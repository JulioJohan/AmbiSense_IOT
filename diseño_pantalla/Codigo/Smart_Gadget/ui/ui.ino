#include <lvgl.h>
#include <TFT_eSPI.h>
#include <ui.h>
#include <TFT_Touch.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include "ui_events.h"


//Wifi setting
const char* ssid = "POCO X3 Pro";
const char* password = "12345678";

WiFiClient espClient;

//MQTT
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;
const char* mqtt_user = "";
const char* mqtt_password = "";
const char* clientID = "";

PubSubClient client(espClient);

//MQTT
const char* MQTT_TOPIC_1 = "utng/pir";
const char* MQTT_TOPIC_2 = "utng/gas";
const char* MQTT_TOPIC_3 = "utng/temp";
const char* MQTT_TOPIC_4 = "utng/humedad";
const char* MQTT_TOPIC_5 = "utng/sonido";
const char* MQTT_TOPIC_6 = "utng/fotoresistencia";

/*Change to your screen resolution*/
static const uint16_t screenWidth  = 320;//480;
static const uint16_t screenHeight = 240;//320;

static lv_disp_draw_buf_t draw_buf;
static lv_color_t buf[ screenWidth * screenHeight/10 ];

TFT_eSPI tft = TFT_eSPI(screenWidth, screenHeight); /* TFT instance */

// These are the pins used to interface between the 2046 touch controller and Arduino Pro
#define DOUT 39  /* Data out pin (T_DO) of touch screen */
#define DIN  32  /* Data in pin (T_DIN) of touch screen */
#define DCS  33  /* Chip select pin (T_CS) of touch screen */
#define DCLK 25  /* Clock pin (T_CLK) of touch screen */

/* Create an instance of the touch screen library */
TFT_Touch touch = TFT_Touch(DCS, DCLK, DIN, DOUT);

#if LV_USE_LOG != 0
/* Serial debugging */
void my_print(const char * buf)
{
    Serial.printf(buf);
    Serial.flush();
}
#endif

/* Display flushing */
void my_disp_flush( lv_disp_drv_t *disp, const lv_area_t *area, lv_color_t *color_p )
{
    uint32_t w = ( area->x2 - area->x1 + 1 );
    uint32_t h = ( area->y2 - area->y1 + 1 );

    tft.startWrite();
    tft.setAddrWindow( area->x1, area->y1, w, h );
    tft.pushColors( ( uint16_t * )&color_p->full, w * h, true );
    tft.endWrite();

    lv_disp_flush_ready( disp );
}

/*Read the touchpad*/

void my_touchpad_read( lv_indev_drv_t * indev_driver, lv_indev_data_t * data )
{
    uint16_t touchX, touchY;

    bool touched = touch.Pressed();//tft.getTouch( &touchX, &touchY, 600 );

    if( !touched )
    {
        data->state = LV_INDEV_STATE_REL;
    }
    else
    {  
        touchX = touch.X();
        touchY = touch.Y();
       
        data->state = LV_INDEV_STATE_PR;

        /*Set the coordinates*/
        data->point.x = touchX;
        data->point.y = touchY;

        Serial.print( "Data x " );
        Serial.println( touchX );

        Serial.print( "Data y " );
        Serial.println( touchY );
    }
}

void setup_wifi() {
    delay(10);
    Serial.println();
    Serial.print("Conectando a ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("Conectado a la red WiFi");
    Serial.println("Dirección IP: " + WiFi.localIP().toString());
}

//Cambiar de lugar
#define MAX_VALUES 50  // Define el máximo de valores que deseas manejar
#define MAX_VALUES_BEFORE_CLEAR 10  // Define la cantidad de veces antes de limpiar

static lv_coord_t ui_gfcTemperatura_series_1_array[MAX_VALUES];
static uint8_t times_temperatura_values_added = 0;

static lv_coord_t ui_gfcSonido_series_1_array[MAX_VALUES];
static uint8_t times_sonido_values_added = 0;

static lv_coord_t ui_gfcLuz_series_1_array[MAX_VALUES];
static uint8_t times_luz_values_added = 0;

static lv_coord_t ui_gfcHumedad_series_1_array[MAX_VALUES];
static uint8_t times_humedad_values_added = 0;

static lv_coord_t ui_gfcGas_series_1_array[MAX_VALUES];
static uint8_t times_gas_values_added = 0;

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Mensaje recibido en el tema: ");
    Serial.println("sd/ventilador");
    Serial.print("Contenido del mensaje: ");
    char mensaje[256];  // Tamaño suficientemente grande para el mensaje
    memset(mensaje, 0, sizeof(mensaje)); // Inicializa el arreglo con ceros
    for (int i = 0; i < length; i++) {
        Serial.print((char)payload[i]);
        mensaje[i] = (char)payload[i]; // Concatenar el carácter al mensaje
    } 

    if (strcmp(topic, MQTT_TOPIC_3) == 0) {
        // Actualiza un elemento de interfaz de usuario con el mensaje del tema 1
        lv_label_set_text(ui_ValorTemperatura, mensaje);
         // Agrega el nuevo valor al array (sin límite)
        for (int i = 0; i < MAX_VALUES; i++) {
            if (ui_gfcTemperatura_series_1_array[i] == 0) {
                ui_gfcTemperatura_series_1_array[i] = atoi(mensaje);  // Suponiendo que el mensaje es numérico
                break;  // Sal del bucle al agregar el valor
            }
        }
        // Aumenta el contador de valores agregados
        times_temperatura_values_added++;
        // Cuando se agreguen 10 valores, limpia el array y reinicia el contador
        if (times_temperatura_values_added >= MAX_VALUES_BEFORE_CLEAR) {
            memset(ui_gfcTemperatura_series_1_array, 0, sizeof(ui_gfcTemperatura_series_1_array));
            times_temperatura_values_added = 0;
        }
        lv_chart_series_t * ui_gfcTemperatura_series_1 = lv_chart_add_series(ui_gfcTemperatura, lv_color_hex(0x808080),
                                                                         LV_CHART_AXIS_PRIMARY_Y);
        // Actualiza el gráfico con los nuevos valores
        lv_chart_set_ext_y_array(ui_gfcTemperatura, ui_gfcTemperatura_series_1, ui_gfcTemperatura_series_1_array);
    } else if (strcmp(topic, MQTT_TOPIC_5) == 0) {
        lv_label_set_text(ui_ValorSonido, mensaje);
        // Agrega el nuevo valor al array (sin límite)
        for (int i = 0; i < MAX_VALUES; i++) {
            if (ui_gfcSonido_series_1_array[i] == 0) {
                ui_gfcSonido_series_1_array[i] = atoi(mensaje);  // Suponiendo que el mensaje es numérico
                break;  // Sal del bucle al agregar el valor
            }
        }
        // Aumenta el contador de valores agregados
        times_sonido_values_added++;
        // Cuando se agreguen 10 valores, limpia el array y reinicia el contador
        if (times_sonido_values_added >= MAX_VALUES_BEFORE_CLEAR) {
            memset(ui_gfcSonido_series_1_array, 0, sizeof(ui_gfcSonido_series_1_array));
            times_sonido_values_added = 0;
        }
        lv_chart_series_t * ui_gfcSonido_series_1 = lv_chart_add_series(ui_gfcSonido, lv_color_hex(0x808080),
                                                                         LV_CHART_AXIS_PRIMARY_Y);
        // Actualiza el gráfico con los nuevos valores
        lv_chart_set_ext_y_array(ui_gfcSonido, ui_gfcSonido_series_1, ui_gfcSonido_series_1_array);
    } else if (strcmp(topic, MQTT_TOPIC_6) == 0) {
        lv_label_set_text(ui_ValorLuz, mensaje);

        for (int i = 0; i < MAX_VALUES; i++) {
            if (ui_gfcLuz_series_1_array[i] == 0) {
                ui_gfcLuz_series_1_array[i] = atoi(mensaje);  // Suponiendo que el mensaje es numérico
                break;  // Sal del bucle al agregar el valor
            }
        }
        // Aumenta el contador de valores agregados
        times_luz_values_added++;
        // Cuando se agreguen 10 valores, limpia el array y reinicia el contador
        if (times_luz_values_added >= MAX_VALUES_BEFORE_CLEAR) {
            memset(ui_gfcLuz_series_1_array, 0, sizeof(ui_gfcLuz_series_1_array));
            times_luz_values_added = 0;
        }
        lv_chart_series_t * ui_gfcLuz_series_1 = lv_chart_add_series(ui_gfcLuz, lv_color_hex(0x808080),
                                                                         LV_CHART_AXIS_PRIMARY_Y);
        // Actualiza el gráfico con los nuevos valores
        lv_chart_set_ext_y_array(ui_gfcLuz, ui_gfcLuz_series_1, ui_gfcLuz_series_1_array);
    }else if (strcmp(topic, MQTT_TOPIC_4) == 0) {
        lv_label_set_text(ui_ValorHumedad, mensaje);
        for (int i = 0; i < MAX_VALUES; i++) {
            if (ui_gfcHumedad_series_1_array[i] == 0) {
                ui_gfcHumedad_series_1_array[i] = atoi(mensaje);  // Suponiendo que el mensaje es numérico
                break;  // Sal del bucle al agregar el valor
            }
        }
        // Aumenta el contador de valores agregados
        times_humedad_values_added++;
        // Cuando se agreguen 10 valores, limpia el array y reinicia el contador
        if (times_humedad_values_added >= MAX_VALUES_BEFORE_CLEAR) {
            memset(ui_gfcHumedad_series_1_array, 0, sizeof(ui_gfcHumedad_series_1_array));
            times_humedad_values_added = 0;
        }
        lv_chart_series_t * ui_gfcHumedad_series_1 = lv_chart_add_series(ui_gfcHumedad, lv_color_hex(0x808080),
                                                                         LV_CHART_AXIS_PRIMARY_Y);
        // Actualiza el gráfico con los nuevos valores
        lv_chart_set_ext_y_array(ui_gfcHumedad, ui_gfcHumedad_series_1, ui_gfcHumedad_series_1_array);
    }else if(strcmp(topic, MQTT_TOPIC_2) == 0){
        if(strcmp(mensaje, "1")==0){
            lv_label_set_text(ui_ValorGas, "Gas detectado");
        }else{
            lv_label_set_text(ui_ValorGas, "Sin gas");
        }
        for (int i = 0; i < MAX_VALUES; i++) {
            if (ui_gfcGas_series_1_array[i] == 0) {
                ui_gfcGas_series_1_array[i] = atoi(mensaje);  // Suponiendo que el mensaje es numérico
                break;  // Sal del bucle al agregar el valor
            }
        }
        // Aumenta el contador de valores agregados
        times_gas_values_added++;
        // Cuando se agreguen 10 valores, limpia el array y reinicia el contador
        if (times_gas_values_added >= MAX_VALUES_BEFORE_CLEAR) {
            memset(ui_gfcGas_series_1_array, 0, sizeof(ui_gfcGas_series_1_array));
            times_gas_values_added = 0;
        }
        lv_chart_series_t * ui_gfcGas_series_1 = lv_chart_add_series(ui_gfcGas, lv_color_hex(0x808080),
                                                                         LV_CHART_AXIS_PRIMARY_Y);
        // Actualiza el gráfico con los nuevos valores
        lv_chart_set_ext_y_array(ui_gfcGas, ui_gfcGas_series_1, ui_gfcGas_series_1_array);        
    }
    Serial.println();
}

void reconnect() {
    while (!client.connected()) {
        Serial.print("Intentando conexión MQTT...");
        if (client.connect(clientID, mqtt_user, mqtt_password)) {
            Serial.println("conectado.");
            client.subscribe("sd/ventilador"); // Reemplazar con el nombre del tema
            client.subscribe(MQTT_TOPIC_1);
            client.subscribe(MQTT_TOPIC_2);
            client.subscribe(MQTT_TOPIC_3);
            client.subscribe(MQTT_TOPIC_4);
            client.subscribe(MQTT_TOPIC_5);
            client.subscribe(MQTT_TOPIC_6);
        } else {
            Serial.print("falló, rc=");
            Serial.print(client.state());
            Serial.println(" intentando de nuevo en 5 segundos.");
            delay(5000);
        }
    }
}



void setup()
{
    Serial.begin( 115200 ); /* prepare for possible serial debug */
    //      
    String LVGL_Arduino = "Hello Arduino! ";
    LVGL_Arduino += String('V') + lv_version_major() + "." + lv_version_minor() + "." + lv_version_patch();

    Serial.println( LVGL_Arduino );
    Serial.println( "I am LVGL_Arduino" );

    lv_init();

#if LV_USE_LOG != 0
    lv_log_register_print_cb( my_print ); /* register print function for debugging */
#endif

    tft.begin();
    tft.setRotation(1);

    touch.setCal(526, 3443, 750, 3377, 320, 240, 1);

    lv_disp_draw_buf_init( &draw_buf, buf, NULL, screenWidth * 10 );

    /*Initialize the display*/
    static lv_disp_drv_t disp_drv;
    lv_disp_drv_init( &disp_drv );
    /*Change the following line to your display resolution*/
    disp_drv.hor_res = screenWidth;
    disp_drv.ver_res = screenHeight;
    disp_drv.flush_cb = my_disp_flush; //刷新
    disp_drv.draw_buf = &draw_buf;
    lv_disp_drv_register( &disp_drv );

    /*Initialize the (dummy) input device driver*/
    static lv_indev_drv_t indev_drv;
    lv_indev_drv_init( &indev_drv );
    indev_drv.type = LV_INDEV_TYPE_POINTER;
    indev_drv.read_cb = my_touchpad_read;
    lv_indev_drv_register( &indev_drv );

#if 0
    /* Create simple label */
    lv_obj_t *label = lv_label_create( lv_scr_act() );
    lv_label_set_text( label, LVGL_Arduino.c_str() );
    lv_obj_align( label, LV_ALIGN_CENTER, 0, 0 );
#else  
    setup_wifi();
    client.setServer(mqtt_server, mqtt_port);
    client.setCallback(callback);
    ui_init();

#endif
    Serial.println( "Setup done" );
}

void loop()
{

    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // Lectura de mensaje desde el monitor serial
    if (Serial.available()) {
        String mensaje = Serial.readStringUntil('\n');
        mensaje.trim();
        
        // Publicar mensaje
        if (mensaje.length() > 0) {
            client.publish("sd/ventilador", mensaje.c_str());
            Serial.println("Mensaje MQTT enviado: " + mensaje);
        }
    }

    lv_timer_handler(); /* let the GUI do its work */
    delay( 5 );
}

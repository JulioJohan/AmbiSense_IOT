SET(SOURCES components/ui_comp_alarm_comp.c
    components/ui_comp_clock_dot.c
    components/ui_comp_scrolldots.c
    components/ui_comp_small_label.c
    components/ui_comp.c
    screens/ui_Splash.c
    screens/ui_Clock.c
    screens/ui_Call.c
    screens/ui_panelTemperatura.c
    screens/ui_panelHumedad.c
    screens/ui_panelSonido.c
    screens/ui_panelLuz.c
    ui.c
    components/ui_comp_hook.c
    ui_helpers.c
    ui_events.cpp
    images/ui_img_ventilador__1png_png.c
    images/ui_img_pattern_png.c
    images/ui_img_2131096662.c
    images/ui_img_728093_png.c
    images/ui_img_sound_png26_png.c
    images/ui_img_1466347900.c
    fonts/ui_font_Number.c)

add_library(ui ${SOURCES})

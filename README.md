# android-reverse-engineer
test task

1. подключил телефон к ПК, открыл на телефоне "Параметры разработчика" и выполнил команду в терминале на пк:
adb shell dumpsys activity activities | grep "mFocused"
вывод: mFocusedApp=ActivityRecord{56ba5ed u0 com.android.settings/.SubSettings} t5644}
  mFocusedWindow=Window{b00f0b7 u0 com.android.settings/com.android.settings.SubSettings}
таким образом имя активити раздела настроек «Параметры разработчика»: 'com.android.settings.SubSettings'

Как вариант, можно было еще воспользоваться AAPT (Android Asset Packaging Tool), предварительно скачав приложение на ПК и вывести активити этого приложения

2. скачал приложение на пк, выполнил команду: aapt dump badging /Users/sam/Downloads/dingtone-6-1-0.apk
Идентификаторприложения: 'me.dingtone.app.im'
Стартовое активити приложения: 'me.dingtone.app.im.activity.SplashActivity'
Перечень разрешений, запрашиваемых приложением:
  'android.permission.SYSTEM_ALERT_WINDOW'
  'android.permission.CALL_PHONE'
  'android.permission.READ_PHONE_STATE'
  'android.permission.READ_PHONE_NUMBERS'
  'android.permission.WRITE_EXTERNAL_STORAGE'
  'android.permission.READ_EXTERNAL_STORAGE'
  'android.permission.VIBRATE'
  'android.permission.INTERNET'
  'android.permission.WAKE_LOCK'
  'android.permission.ACCESS_WIFI_STATE'
  'android.permission.ACCESS_NETWORK_STATE'
  'android.permission.CAMERA'
  'android.permission.RECORD_AUDIO'
  'android.permission.READ_CONTACTS'
  'android.permission.WRITE_CONTACTS'
  'android.permission.MODIFY_AUDIO_SETTINGS'
  'android.permission.BLUETOOTH'
  'android.permission.FOREGROUND_SERVICE'
  'android.permission.RECEIVE_BOOT_COMPLETED'
  'android.permission.ACCESS_FINE_LOCATION'
  'android.permission.ACCESS_COARSE_LOCATION'
  'android.permission.SCHEDULE_EXACT_ALARM'
  'com.google.android.gms.permission.AD_ID'
  'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE'
  'com.google.android.c2dm.permission.RECEIVE'
  'com.android.vending.BILLING'

3. в репозитории файл main.py

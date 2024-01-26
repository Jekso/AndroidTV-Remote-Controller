
from enum import Enum



class AndroidTVApps(Enum):
    """
    Enum class for many famous used apps for Android TV
    
    To get main activity name use `adb_client.get_package_activities(package_name)`
    and try to interpret the output dump to extract the main launcher activity 
    then you can use these values for `controller.open_app(package_name, activity_name)` method.
    """
    CHROME = 'com.android.chrome/com.google.android.apps.chrome.Main'
    YOUTUBE = 'com.google.android.youtube.tv/com.google.android.apps.youtube.tv.activity.ShellActivity'
    NETFLIX = 'com.netflix.ninja/.MainActivity'
    AMAZON_PRIME = 'com.amazon.amazonvideo.livingroom/com.amazon.ignition.IgnitionActivity'
    WATCH_IT = 'com.watchit.vod/.refactor.splash.ui.SplashActivity'

    # ..
    # feel free to add your own custom tv apps 'package/main_activity'
    # to get main activity name use adb.get_package_activities(package_name)
    # and try to interpret the output dump to extract the main launcher activity 
    # then you can use these values for controller.open_app() method.
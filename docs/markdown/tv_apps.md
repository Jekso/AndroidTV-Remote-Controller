Module AndroidTVController.tv_apps
==================================

Classes
-------

`AndroidTVApps(*args, **kwds)`
:   Enum class for many famous used apps for Android TV
    
    To get main activity name use `adb_client.get_package_activities(package_name)`
    and try to interpret the output dump to extract the main launcher activity 
    then you can use these values for `controller.open_app(package_name, activity_name)` method.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `AMAZON_PRIME`
    :

    `CHROME`
    :

    `NETFLIX`
    :

    `WATCH_IT`
    :

    `YOUTUBE`
    :
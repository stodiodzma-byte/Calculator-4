[app]
title = Calculator
package.name = calculator
package.domain = org.zard.studio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# إعدادات أندرويد الأساسية للسيرفر
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 24
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False
android.fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

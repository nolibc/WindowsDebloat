import winreg
import subprocess


class Optimizations:
    def dotnet_framework(self):
        print("\n[*] Installing .NET Framework 3.5...")
        subprocess.run(
            "powershell.exe DISM /Online /Enable-Feature /FeatureName:NetFx3 /All"
        )
        print("\n[*] .NET Framework 3.5 installed.")

    def disable_mouse_acceleration(self):
        MOUSE_SENS = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Control Panel\Mouse")
        winreg.SetValueEx(MOUSE_SENS, "MouseSensitivity", 0, winreg.REG_SZ, "10")
        winreg.SetValueEx(
            MOUSE_SENS,
            "SmoothMouseXCurve",
            0,
            winreg.REG_BINARY,
            bytes.fromhex(
                "00 00 00 00 00 00 00 00"
                "C0 CC 0C 00 00 00 00 00"
                "80 99 19 00 00 00 00 00"
                "40 66 26 00 00 00 00 00"
                "00 33 33 00 00 00 00 00"
            ),
        )
        winreg.SetValueEx(
            MOUSE_SENS,
            "SmoothMouseYCurve",
            0,
            winreg.REG_BINARY,
            bytes.fromhex(
                "00 00 00 00 00 00 00 00"
                "00 00 38 00 00 00 00 00"
                "00 00 70 00 00 00 00 00"
                "00 00 A8 00 00 00 00 00"
                "00 00 E0 00 00 00 00 00"
            ),
        )
        winreg.CloseKey(MOUSE_SENS)

        MOUSE_THRESHHOLD = winreg.CreateKey(  # Disable enhance pointer precision
            winreg.HKEY_USERS, ".DEFAULT\Control Panel\Mouse"
        )
        winreg.SetValueEx(MOUSE_THRESHHOLD, "MouseSpeed", 0, winreg.REG_SZ, "0")
        winreg.SetValueEx(MOUSE_THRESHHOLD, "MouseThreshold1", 0, winreg.REG_SZ, "0")
        winreg.SetValueEx(MOUSE_THRESHHOLD, "MouseThreshold2", 0, winreg.REG_SZ, "0")
        winreg.CloseKey(MOUSE_THRESHHOLD)
        print("\n[*] Mouse acceleration disabled.")

    def fix_keyboard_input_delay(self):
        KEYBOARD_DELAY_USER = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Control Panel\Keyboard"
        )
        winreg.SetValueEx(KEYBOARD_DELAY_USER, "KeyboardDelay", 0, winreg.REG_SZ, "0")
        winreg.CloseKey(KEYBOARD_DELAY_USER)

        KEYBOARD_DELAY_DEFAULT = winreg.CreateKey(
            winreg.HKEY_USERS, ".DEFAULT\Control Panel\Keyboard"
        )
        winreg.SetValueEx(
            KEYBOARD_DELAY_DEFAULT, "KeyboardDelay", 0, winreg.REG_SZ, "0"
        )
        winreg.CloseKey(KEYBOARD_DELAY_DEFAULT)
        print("\n[*] Fixed Keyboard Input Delay.")

    def disable_hibernation(self):
        subprocess.run("powercfg.exe /h off", shell=True)
        print("[*] Hibernation disabled.")

    def ultimate_power_plan(self):
        subprocess.run(
            "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61",
            shell=True,
        )
        print("\n[*] Ultimate power plan enabled. (Check 'Edit Power Plan' settings.")

    def performance_tweaks(self):
        CPU_SLEEP = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\943c8cb6-6f93-4227-ad87-e9a3feec08d1",
        )
        winreg.SetValueEx(CPU_SLEEP, "Attributes", 0, winreg.REG_SZ, "2")
        winreg.CloseKey(CPU_SLEEP)

        GPU_PRIORITY = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile",
        )
        # GPU priority
        winreg.SetValueEx(GPU_PRIORITY, "Affinity", 0, winreg.REG_DWORD, 0x00000000)
        print("[*] Affinity set to 0")
        winreg.SetValueEx(GPU_PRIORITY, "Background Only", 0, winreg.REG_SZ, "False")
        print("Background Only set to 0")
        winreg.SetValueEx(GPU_PRIORITY, "Clock Rate", 0, winreg.REG_DWORD, 0x00002710)
        print("[*] Clock Rate set to 00002710")
        winreg.SetValueEx(GPU_PRIORITY, "GPU Priority", 0, winreg.REG_DWORD, 0x00000008)
        print("[*] GPU Priority set to 00000008")
        winreg.SetValueEx(GPU_PRIORITY, "Priority", 0, winreg.REG_DWORD, 0x00000006)
        print("[*] Priority set to 00000006")
        winreg.SetValueEx(GPU_PRIORITY, "Scheduling Category", 0, winreg.REG_SZ, "High")
        print("[*] Scheduling Category set to High")
        winreg.SetValueEx(GPU_PRIORITY, "SFIO Priority", 0, winreg.REG_SZ, "High")
        print("[*] SFIO Priority set to High")
        winreg.CloseKey(GPU_PRIORITY)
        # System responsiveness
        SYSTEM_RESPONSIVENESS = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile",
        )
        winreg.SetValueEx(
            SYSTEM_RESPONSIVENESS,
            "SystemResponsiveness",
            0,
            winreg.REG_DWORD,
            0x0000000A,
        )
        winreg.SetValueEx(
            SYSTEM_RESPONSIVENESS,
            "NetworkThrottlingIndex",
            0,
            winreg.REG_DWORD,
            0xFFFFFFF,
        )
        winreg.CloseKey(SYSTEM_RESPONSIVENESS)

        # RAM management
        RAM_MANAGER = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop"
        )
        winreg.SetValueEx(RAM_MANAGER, "AutoEndTasks", 0, winreg.REG_SZ, "1")
        winreg.SetValueEx(RAM_MANAGER, "HungAppTimeout", 0, winreg.REG_SZ, "1000")
        winreg.SetValueEx(RAM_MANAGER, "MenuShowDelay", 0, winreg.REG_SZ, "8")
        winreg.SetValueEx(RAM_MANAGER, "WaitToKillAppTimeout", 0, winreg.REG_SZ, "2000")
        winreg.SetValueEx(RAM_MANAGER, "LowLevelHooksTimeout", 0, winreg.REG_SZ, "1000")
        winreg.CloseKey(RAM_MANAGER)
        # Decrease shutdown time
        SHUTDOWN_TIME = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control"
        )
        winreg.SetValueEx(
            SHUTDOWN_TIME, "WaitToKillServiceTimeout", 0, winreg.REG_SZ, "2000"
        )
        winreg.CloseKey(SHUTDOWN_TIME)

        ENERGY_ESTIMATE = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Power"
        )
        winreg.SetValueEx(
            ENERGY_ESTIMATE, "EnergyEstimationEnabled", 0, winreg.REG_DWORD, 0x00000000
        )
        print("[*] System responsiveness tweaks applied")
        # Change Windows Updates to "Notify to schedule restart"
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" /v UxOption /t REG_DWORD /d 1 /f'
        )
        print("[*] Changed Windows Updates to Notify to schedule restart")
        # Disable P2P Update downlods outside of local network
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\DeliveryOptimization\\Config" /v DODownloadMode /t REG_DWORD /d 0 /f'
        )
        print("[*] Disabled P2P Update downloads outside of local network")

    def visual_tweaks(self):
        DPI_SCALING = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop"
        )
        winreg.SetValueEx(
            DPI_SCALING, "Win8DpiScaling", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.SetValueEx(DPI_SCALING, "DpiScalingVer", 0, winreg.REG_DWORD, 0x00001000)
        winreg.SetValueEx(DPI_SCALING, "LogPixels", 0, winreg.REG_DWORD, 0x00000096)
        winreg.CloseKey(DPI_SCALING)
        print("[*] Disabled WinDPI Scaling")

        ANIMATIONS = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
        )
        winreg.SetValueEx(
            ANIMATIONS, "ExtendedUIHoverTime", 0, winreg.REG_DWORD, 0x00030000
        )
        winreg.SetValueEx(ANIMATIONS, "DontPrettyPath", 0, winreg.REG_DWORD, 0x00000001)
        winreg.SetValueEx(ANIMATIONS, "ListviewShadow", 0, winreg.REG_DWORD, 0x00000000)
        winreg.SetValueEx(
            ANIMATIONS, "TaskbarAnimations", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(ANIMATIONS)

        AERO_PEEK = winreg.CreateKey(
            winreg.HKEY_CURRENT_CONFIG, "Software\\Microsoft\\Windows\\DWM"
        )
        winreg.SetValueEx(AERO_PEEK, "EnableAeroPeek", 0, winreg.REG_DWORD, 0x00000000)
        winreg.CloseKey(AERO_PEEK)

        DISALLOW_SHAKING = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
        )
        winreg.SetValueEx(
            DISALLOW_SHAKING, "DisallowShaking", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.CloseKey(DISALLOW_SHAKING)

        TRANSITIONS = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Policies\\Microsoft\\Windows\\DWM"
        )
        winreg.SetValueEx(
            TRANSITIONS,
            "DWMWA_TRANSITIONS_FORCEDISABLED",
            0,
            winreg.REG_DWORD,
            0x00000001,
        )
        winreg.SetValueEx(
            TRANSITIONS, "DisallowAnimations", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.CloseKey(TRANSITIONS)

        FONT_SMOOTHING = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop"
        )
        winreg.SetValueEx(FONT_SMOOTHING, "FontSmoothing", 0, winreg.REG_SZ, "2")
        winreg.SetValueEx(
            FONT_SMOOTHING, "FontSmoothingType", 0, winreg.REG_DWORD, 0x00000002
        )
        winreg.CloseKey(FONT_SMOOTHING)

        ALL_UP_VIEW = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MultitaskingView\\AllUpView",
        )
        winreg.SetValueEx(ALL_UP_VIEW, "AllUpView", 0, winreg.REG_DWORD, 0x00000000)
        winreg.SetValueEx(
            ALL_UP_VIEW, "Remove TaskView", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.CloseKey(ALL_UP_VIEW)
        ANIMATE_LIMITS = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop\\WindowMetrics"
        )
        winreg.SetValueEx(ANIMATE_LIMITS, "MinAnimate", 0, winreg.REG_SZ, "0")
        winreg.SetValueEx(ANIMATE_LIMITS, "MaxAnimate", 0, winreg.REG_SZ, "0")
        winreg.CloseKey(ANIMATE_LIMITS)

        FILE_EXPLORER = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
        )
        winreg.SetValueEx(
            FILE_EXPLORER, "NoLowDiskSpaceChecks", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.SetValueEx(
            FILE_EXPLORER, "LinkResolveIgnoreLinkInfo", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.SetValueEx(
            FILE_EXPLORER, "NoResolveSearch", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.SetValueEx(
            FILE_EXPLORER, "NoResolveTrack", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.SetValueEx(
            FILE_EXPLORER, "NoInternetOpenWith", 0, winreg.REG_DWORD, 0x00000001
        )
        winreg.CloseKey(FILE_EXPLORER)
        print("[*] Visual Tweaks applied")


class Debloat:
    def disable_bloat_services(self):
        subprocess.run("sc stop DiagTrack")
        print("\n[*] DiagTrack service stopped")
        subprocess.run("sc stop diagnosticshub.standardcollector.service")
        print("[*] Diagnosticshub service stopped")
        subprocess.run("sc stop dmwappushservice")
        print("[*] dmwappushservice stopped")
        subprocess.run("sc stop WMPNetworkSvc")
        print("[*] WMPNetworkSvc stopped")
        subprocess.run("sc stop WSearch")
        subprocess.run("sc config DiagTrack start= disabled")
        subprocess.run(
            "sc config diagnosticshub.standardcollector.service start= disabled"
        )
        subprocess.run("sc config dmwappushservice start= disabled")
        subprocess.run("sc config WMPNetworkSvc start= disabled")
        subprocess.run("sc config WSearch start= disabled")
        subprocess.run(
            'schtasks /Change /TN "Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser" /Disable'
        )
        subprocess.run(
            'schtasks /Change /TN "Microsoft\\Windows\\Application Experience\\ProgramDataUpdater" /Disable'
        )
        subprocess.run(
            'schtasks /Change /TN "Microsoft\\Windows\\Application Experience\\StartupAppTask" /Disable'
        )
        subprocess.run(
            'schtasks /Change /TN "Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator" /Disable'
        )
        subprocess.run(
            'schtasks /Change /TN "Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip" /Disable'
        )

    def disable_gamedvr(self):
        GAMEDVR = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "System\\GameConfigStore")
        winreg.SetValueEx(GAMEDVR, "GameDVR_Enabled", 0, winreg.REG_DWORD, 0x00000000)
        winreg.SetValueEx(
            GAMEDVR, "GameDVR_FSEBehaviorMode", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.SetValueEx(
            GAMEDVR,
            "Win32_AutoGameModeDefaultProfile",
            0,
            winreg.REG_BINARY,
            bytes.fromhex(
                "00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00"
            ),
        )
        winreg.SetValueEx(
            GAMEDVR,
            "Win32_GameModeRelatedProcesses",
            0,
            winreg.REG_BINARY,
            bytes.fromhex(
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                "00 00 00 00 00 00 00 00 00 00"
            ),
        )
        winreg.SetValueEx(
            GAMEDVR, "GameDVR_HonorUserFSEBehaviorMode", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.SetValueEx(
            GAMEDVR,
            "GameDVR_DXGIHonorFSEWindowsCompatible",
            0,
            winreg.REG_DWORD,
            0x00000000,
        )
        winreg.SetValueEx(
            GAMEDVR, "GameDVR_EFSEFeatureFlags", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(GAMEDVR)

        ALLOW_GAMEDVR = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR"
        )
        winreg.SetValueEx(ALLOW_GAMEDVR, "AllowGameDVR", 0, winreg.REG_SZ, "0")
        winreg.CloseKey(ALLOW_GAMEDVR)

        GAMEMODE = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\GameBar"
        )
        winreg.SetValueEx(
            GAMEMODE, "AllowAutoGameMode", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.SetValueEx(
            GAMEMODE, "AutoGameModeEnabled", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(GAMEMODE)

        APPLICATION_MANAGEMENT = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR",
        )
        winreg.SetValueEx(APPLICATION_MANAGEMENT, "value", 0, winreg.REG_SZ, "00000000")
        winreg.CloseKey(APPLICATION_MANAGEMENT)

        GAME_BAR = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\GameBar"
        )
        winreg.SetValueEx(
            GAME_BAR, "UseNexusForGameBarEnabled", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(GAME_BAR)

        APP_CAPTURE_GAMEDVR = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
        )
        winreg.SetValueEx(
            APP_CAPTURE_GAMEDVR, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(APP_CAPTURE_GAMEDVR)

    def remove_telemetry_keys(self):
        APPLICATION_TELEMETRY = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy",
        )
        winreg.SetValueEx(
            APPLICATION_TELEMETRY,
            "DisableTaggedEnergyLogging",
            0,
            winreg.REG_DWORD,
            0x00000001,
        )
        winreg.SetValueEx(
            APPLICATION_TELEMETRY,
            "TelemetryMaxApplication",
            0,
            winreg.REG_DWORD,
            0x00000000,
        )
        winreg.SetValueEx(
            APPLICATION_TELEMETRY,
            "TelemetryMaxTagPerApplication",
            0,
            winreg.REG_DWORD,
            0x00000000,
        )
        winreg.CloseKey(APPLICATION_TELEMETRY)

        NO_INSTRUMENTATION_MACHINE = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
        )
        winreg.SetValueEx(
            NO_INSTRUMENTATION_MACHINE,
            "NoInstrumentation",
            0,
            winreg.REG_DWORD,
            0x00000001,
        )
        winreg.CloseKey(NO_INSTRUMENTATION_MACHINE)

        NO_INSTRUMENTATION_USER = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
        )
        winreg.SetValueEx(
            NO_INSTRUMENTATION_USER,
            "NoInstrumentation",
            0,
            winreg.REG_DWORD,
            0x00000001,
        )
        winreg.CloseKey(NO_INSTRUMENTATION_USER)

        CEIP_ENABLE = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Policies\\Microsoft\\SQMClient\\Windows",
        )
        winreg.SetValueEx(CEIP_ENABLE, "CEIPEnable", 0, winreg.REG_DWORD, 0x00000000)
        winreg.CloseKey(CEIP_ENABLE)

        PREVENT_HANDWRITING_ERROR_REPORTS = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Policies\\Microsoft\\Windows\\HandwritingErrorReports",
        )
        winreg.SetValueEx(
            PREVENT_HANDWRITING_ERROR_REPORTS,
            "PreventHandwritingErrorReports",
            0,
            winreg.REG_DWORD,
            0x00000001,
        )
        winreg.CloseKey(PREVENT_HANDWRITING_ERROR_REPORTS)

        ALLOW_TELEMETRY_MS = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection",
        )
        winreg.SetValueEx(
            ALLOW_TELEMETRY_MS, "AllowTelemetry", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(ALLOW_TELEMETRY_MS)

        ALLOW_TELEMETRY_POLICY = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection",
        )
        winreg.SetValueEx(
            ALLOW_TELEMETRY_POLICY, "AllowTelemetry", 0, winreg.REG_DWORD, 0x00000000
        )
        winreg.CloseKey(ALLOW_TELEMETRY_POLICY)

        AIT_ENABLE = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat",
        )
        winreg.SetValueEx(AIT_ENABLE, "AITEnable", 0, winreg.REG_DWORD, 0x00000000)
        winreg.CloseKey(AIT_ENABLE)

        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Device Metadata" /v PreventDeviceMetadataFromNetwork /t REG_DWORD /d 1 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\MRT" /v DontOfferThroughWUAU /t REG_DWORD /d 1 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\SQMClient\\Windows" /v "CEIPEnable" /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat" /v "AITEnable" /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat" /v "DisableUAR" /t REG_DWORD /d 1 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\AutoLogger-Diagtrack-Listener" /v "Start" /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\SQMLogger" /v "Start" /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AppHost" /v EnableWebContentEvaluation /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\Software\\Microsoft\\PolicyManager\\default\\WiFi\\AllowWiFiHotSpotReporting" /v value /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKLM\\Software\\Microsoft\\PolicyManager\\default\\WiFi\AllowAutoConnectToWiFiSenseHotspots" /v value /t REG_DWORD /d 0 /f'
        )
        subprocess.run(
            'reg add "HKCU\\Control Panel\\International\\User Profile" /v HttpAcceptLanguageOptOut /t REG_DWORD /d 1 /f'
        )

    def uninstall_ms_apps(self):  # Choose which Microsoft default apps to uninstall
        try:
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *3DBuilder* | Remove-AppxPackage"',
                shell=True,
            )  # 3D Builder
            print("[*] Uninstalled 3D Builder")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *Getstarted* | Remove-AppxPackage"',
                shell=True,
            )  # Get Started
            print("[*] Uninstalled Get Started")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *WindowsAlarms* | Remove-AppxPackage"',
                shell=True,
            )  # Windows Alarms App
            print("[*] Uninstalled Windows Alarms App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *WindowsCamera* | Remove-AppxPackage"',
                shell=True,
            )  # Windows Camera App
            print("[*] Uninstalled Windows Camera App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *bing* | Remove-AppxPackage"',
                shell=True,
            )  # Bing
            print("[*] Uninstalled Bing")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *MicrosoftOfficeHub* | Remove-AppxPackage"',
                shell=True,
            )  # Microsoft Office Hub
            print("[*] Uninstalled Microsoft Office Hub")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *OneNote* | Remove-AppxPackage"',
                shell=True,
            )  # OneNote
            print("[*] Uninstalled OneNote")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *WindowsPhone* | Remove-AppxPackage"',
                shell=True,
            )  # Windows Phone
            print("[*] Uninstalled Windows Phone")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *photos* | Remove-AppxPackage"',
                shell=True,
            )  # Photos App
            print("[*] Uninstalled Photos App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *SkypeApp* | Remove-AppxPackage"',
                shell=True,
            )  # Skype App
            print("[*] Uninstalled Skype App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *solit* | Remove-AppxPackage"',
                shell=True,
            )  # Solit App
            print("[*] Uninstalled Solit App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *WindowsSoundRecorder* | Remove-AppxPackage"',
                shell=True,
            )  # Windows Sound Recorder App
            print("[*] Uninstalled Windows Sound Recorder App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage"',
                shell=True,
            )  # Windows Communications Apps
            print("[*] Uninstalled Windows Communications Apps")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *zune* | Remove-AppxPackage"',
                shell=True,
            )  # Zune App
            print("[*] Uninstalled Zune App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *WindowsMaps* | Remove-AppxPackage"',
                shell=True,
            )  # Windows Maps
            print("[*] Uninstalled Windows Maps")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *Sway* | Remove-AppxPackage"',
                shell=True,
            )  # Sway App
            print("[*] Uninstalled Sway App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *CommsPhone* | Remove-AppxPackage"',
                shell=True,
            )  # CommsPhone
            print("[*] Uninstalled CommsPhone")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *ConnectivityStore* | Remove-AppxPackage"',
                shell=True,
            )  # Connectivity Store - NOT Windows Store
            print("[*] Uninstalled Connectivity Store - NOT Windows Store")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *Microsoft.Messaging* | Remove-AppxPackage"',
                shell=True,
            )  # Microsoft Messaging App
            print("[*] Uninstalled Microsoft Messaging App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *Facebook* | Remove-AppxPackage"',
                shell=True,
            )  # Facebook App
            print("[*] Uninstalled Facebook App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *Twitter* | Remove-AppxPackage"',
                shell=True,
            )  # Twitter App
            print("[*] Uninstalled Twitter App")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *Drawboard PDF* | Remove-AppxPackage"',
                shell=True,
            )  # Drawboard PDF
            print("[*] Uninstalled Drawboard PDF")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *YourPhone* | Remove-AppxPackage"',
                shell=True,
            )  # Your Phone
            print("[*] Uninstalled Your Phone")
            subprocess.run(
                'PowerShell -Command "Get-AppxPackage *XboxApp* | Remove-AppxPackage"',
                shell=True,
            )  # XBox App
            print("[*] Uninstalled XBox App")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *XboxIdentityProvider* | Remove-AppxPackage"',
                shell=True,
            )  # # XBox Identity
            print("[*] Uninstalled XBox Identity")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Xbox.TCUI* | Remove-AppxPackage" ',
                shell=True,
            )  # XBox Live
            print("[*] Uninstalled XBox Live")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *XboxSpeechToTextOverlay* | Remove-AppxPackage"',
                shell=True,
            )  # XBox Overlay
            print("[*] Uninstalled XBox Overlay")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *XboxGamingOverlay* | Remove-AppxPackage"',
                shell=True,
            )  # XBox Game Bar
            print("[*] Uninstalled XBox Game Bar")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *XboxGameOverlay* | Remove-AppxPackage"',
                shell=True,
            )  # XBox Game Bar
            print("[*] Uninstalled XBox Game Bar")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *MicrosoftStickyNotes* | Remove-AppxPackage"',
                shell=True,
            )  # Sticky Notes
            print("[*] Uninstalled Sticky Notes")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.ScreenSketch* | Remove-AppxPackage"',
                shell=True,
            )  # Snip and Sketch
            print("[*] Uninstalled Snip and Sketch")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.MSPaint* | Remove-AppxPackage"',
                shell=True,
            )  # Paint 3D - NOT actual MS Paint
            print("[*] Uninstalled Paint 3D - NOT actual MS Paint")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.Wallet* | Remove-AppxPackage"',
                shell=True,
            )  # Microsoft Pay
            print("[*] Uninstalled Microsoft Pay")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.GetHelp* | Remove-AppxPackage"',
                shell=True,
            )  # Get Help
            print("[*] Uninstalled Get Help")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.WindowsFeedbackHub* | Remove-AppxPackage"',
                shell=True,
            )  # Feedback Hub
            print("[*] Uninstalled Feedback Hub")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.People* | Remove-AppxPackage"',
                shell=True,
            )  #  People
            print("[*] Uninstalled People")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.Microsoft3DViewer* | Remove-AppxPackage"',
                shell=True,
            )  # 3D Viewer
            print("[*] Uninstalled 3D Viewer")
            subprocess.run(
                'Powershell -Command "Get-AppxPackage *Microsoft.MixedReality.Portal* | Remove-AppxPackage"',
                shell=True,
            )  # Mixed Reality Portal
            print("[*] Uninstalled Mixed Reality Portal")

        except Exception:
            print("[*] Error: Microsoft Apps may already be uninstalled.")

    def uninstall_ms_onedrive(self):
        try:
            subprocess.run(
                'set x86="%SYSTEMROOT%\\System32\\OneDriveSetup.exe"', shell=True
            )
            subprocess.run(
                'set x64="%SYSTEMROOT%\\SysWOW64\\OneDriveSetup.exe"', shell=True
            )
            print("Closing OneDrive process..\n")
            subprocess.run("taskkill /f /im OneDrive.exe > NUL 2>&1", shell=True)
            subprocess.run("ping 127.0.0.1 -n 5 > NUL 2>&1", shell=True)
            print("Uninstalling OneDrive\n")
            subprocess.run(
                "%SystemRoot%\\SysWOW64\\OneDriveSetup.exe /uninstall", shell=True
            )
            subprocess.run("ping 127.0.0.1 -n 10 > NUL 2>&1", shell=True)
            print("Removing OneDrive leftovers..\n")
            subprocess.run('rd "%USERPROFILE%\\OneDrive" /Q /S > NUL 2>&1', shell=True)
            subprocess.run('rd "C:\\OneDriveTemp" /Q /S > NUL 2>&1', shell=True)
            subprocess.run(
                'rd "%LOCALAPPDATA%\\Microsoft\\OneDrive" /Q /S > NUL 2>&1', shell=True
            )
            subprocess.run(
                'rd "%PROGRAMDATA%\\Microsoft OneDrive" /Q /S > NUL 2>&1', shell=True
            )
            print("Removing OneDrive from the Explorer Side Panel..")
            subprocess.run(
                'REG DELETE "HKEY_CLASSES_ROOT\\CLSID\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" /f > NUL 2>&1',
                shell=True,
            )
            subprocess.run(
                'REG DELETE "HKEY_CLASSES_ROOT\\Wow6432Node\\CLSID\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" /f > NUL 2>&1',
                shell=True,
            )
            print("[*] OneDrive has been uninstalled.\n")
        except Exception:
            print("[*] Error: Could not uninstall Microsoft OneDrive.\n")

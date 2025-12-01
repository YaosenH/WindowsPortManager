PROCESS_DATA = {
    "svchost.exe": {
        "description": "Windows 服务宿主进程，用于承载各种系统 DLL 服务（如网络、音频、Windows 更新等）。",
        "importance": "不建议kill"
    },
    "System": {
        "description": "Windows 内核进程，处理大多数内核级线程和驱动程序操作。",
        "importance": "不可kill"
    },
    "vmware-authd.exe": {
        "description": "VMware 授权服务，用于管理虚拟机及其权限。",
        "importance": "可以kill"
    },
    "jhi_service.exe": {
        "description": "Intel Dynamic Application Loader Host Interface Service，英特尔驱动相关服务。",
        "importance": "不建议kill"
    },
    "wetype_server.exe": {
        "description": "微信输入法（WeType）的核心服务进程。",
        "importance": "可以kill"
    },
    "services.exe": {
        "description": "Windows 服务控制管理器，负责启动、停止和与系统服务交互。",
        "importance": "不可kill"
    },
    "frpc.exe": {
        "description": "FRP (Fast Reverse Proxy) 客户端，用于内网穿透。",
        "importance": "可以kill"
    },
    "wetype_update.exe": {
        "description": "微信输入法的自动更新进程。",
        "importance": "可以kill"
    },
    "GameViewerServer.exe": {
        "description": "网易 GameViewer 远程控制/游戏串流软件的服务端。",
        "importance": "可以kill"
    },
    "ollama app.exe": {
        "description": "Ollama 本地大模型运行工具的应用程序主进程。",
        "importance": "可以kill"
    },
    "Antigravity.exe": {
        "description": "通常是网易游戏或相关启动器（如UU加速器、部分网易游戏）的下载/更新组件。",
        "importance": "可以kill"
    },
    "wetype_renderer.exe": {
        "description": "微信输入法的界面渲染进程。",
        "importance": "可以kill"
    },
    "verge-mihomo.exe": {
        "description": "Clash Verge 的内核进程（Mihomo），负责网络代理流量转发。",
        "importance": "可以kill"
    },
    "msedgewebview2.exe": {
        "description": "Microsoft Edge WebView2 控件，被其他程序（如输入法、Clash Verge）用来显示网页内容。",
        "importance": "可以kill"
    },
    "SangforPromoteService.exe": {
        "description": "深信服（Sangfor）EasyConnect VPN 的推广/辅助服务。",
        "importance": "可以kill"
    },
    "ECAgent.exe": {
        "description": "EasyConnect Agent，深信服 VPN 客户端的核心代理程序。",
        "importance": "可以kill"
    },
    "System Idle Process": {
        "description": "系统空闲进程，显示 CPU 空闲时间的百分比，并非真正的进程。",
        "importance": "不可kill"
    },
    "language_server_windows_x64.exe": {
        "description": "语言服务器协议进程，通常由代码编辑器（如 VSCode, Cursor）启动以提供代码补全功能。",
        "importance": "可以kill"
    },
    "python.exe": {
        "description": "Python 解释器进程，正在运行 Python 脚本。",
        "importance": "可以kill"
    },
    "mysqld.exe": {
        "description": "MySQL 数据库服务端进程。",
        "importance": "可以kill"
    },
    "chrome.exe": {
        "description": "Google Chrome 浏览器进程。",
        "importance": "可以kill"
    },
    "mDNSResponder.exe": {
        "description": "Bonjour 服务，用于局域网内的设备和打印机发现（多播DNS）。",
        "importance": "不建议kill"
    },
    "ToDesk.exe": {
        "description": "ToDesk 远程控制软件主程序。",
        "importance": "可以kill"
    },
    "redis-server.exe": {
        "description": "Redis 内存数据库服务端进程。",
        "importance": "可以kill"
    },
    "clash-verge.exe": {
        "description": "Clash Verge 代理工具的图形界面主程序。",
        "importance": "可以kill"
    },
    "ollama.exe": {
        "description": "Ollama 的后台服务进程，用于加载和推理 AI 模型。",
        "importance": "可以kill"
    },
    "lsass.exe": {
        "description": "本地安全机构子系统服务，负责用户登录验证和安全策略。结束它会导致系统重启。",
        "importance": "不可kill"
    },
    "wininit.exe": {
        "description": "Windows 启动初始化进程，负责启动关键后台服务。结束它会导致蓝屏。",
        "importance": "不可kill"
    },
    "spoolsv.exe": {
        "description": "打印后台处理程序服务，负责管理打印任务。",
        "importance": "不建议kill"
    },
    "clash-core-service.exe": {
        "description": "Clash 核心服务模式进程。",
        "importance": "可以kill"
    },
    "SangforUDProtectEx.exe": {
        "description": "深信服（Sangfor）的安全防护或防卸载进程，通常与 EasyConnect 相关。",
        "importance": "不建议kill"
    },
    "HipsDaemon.exe": {
        "description": "主机入侵防御系统守护进程，通常属于杀毒软件或企业VPN（如深信服）的一部分。",
        "importance": "不建议kill"
    },
    "smss.exe": {
    "进程名": "smss.exe",
    "进程描述": "Windows 会话管理器子系统 (Session Manager Subsystem)。负责启动用户会话。结束它会导致蓝屏死机。",
    "重要性": "不可kill"
    },
    "csrss.exe": {
    "进程名": "csrss.exe",
    "进程描述": "客户端/服务器运行时子系统 (Client Server Runtime Process)。负责控制台窗口和创建/删除线程。结束它会导致蓝屏死机。",
    "重要性": "不可kill"
    },
    "explorer.exe": {
    "进程名": "explorer.exe",
    "进程描述": "Windows 资源管理器。负责显示任务栏、桌面图标和文件夹窗口。结束它会导致桌面和任务栏消失（可重启恢复）。",
    "重要性": "不建议kill"
    },
    "dwm.exe": {
    "进程名": "dwm.exe",
    "进程描述": "桌面窗口管理器 (Desktop Window Manager)。负责处理窗口特效、透明度等图形界面渲染。",
    "重要性": "不建议kill"
    },
    "MsMpEng.exe": {
    "进程名": "MsMpEng.exe",
    "进程描述": "Microsoft Defender Antivirus Service。Windows 自带杀毒软件的核心引擎，负责实时扫描。",
    "重要性": "不建议kill"
    },
    "WmiPrvSE.exe": {
    "进程名": "WmiPrvSE.exe",
    "进程描述": "WMI Provider Host。为软件提供系统管理信息。如果占用 CPU 过高通常意味着有程序在频繁查询系统信息。",
    "重要性": "不建议kill"
    },
    "RuntimeBroker.exe": {
    "进程名": "RuntimeBroker.exe",
    "进程描述": "用于管理 Windows Store 应用（UWP应用）的权限（如相机、位置）。",
    "重要性": "可以kill"
    },
    "taskmgr.exe": {
    "进程名": "taskmgr.exe",
    "进程描述": "Windows 任务管理器主程序。",
    "重要性": "可以kill"
    },
    "SearchIndexer.exe": {
    "进程名": "SearchIndexer.exe",
    "进程描述": "Microsoft Windows Search 索引器。负责为文件建立索引以便快速搜索。结束它会暂时停止索引。",
    "重要性": "可以kill"
    },
    "ctfmon.exe": {
    "进程名": "ctfmon.exe",
    "进程描述": "CTF 加载程序。负责控制替代用户输入文本输入处理器（输入法、语言栏）。结束它可能导致无法输入中文。",
    "重要性": "不建议kill"
    },
    "WeChat.exe": {
    "进程名": "WeChat.exe",
    "进程描述": "微信 PC 版主程序。",
    "重要性": "可以kill"
    },
    "QQ.exe": {
    "进程名": "QQ.exe",
    "进程描述": "QQ PC 版主程序。",
    "重要性": "可以kill"
    },
    "DingTalk.exe": {
    "进程名": "DingTalk.exe",
    "进程描述": "钉钉 PC 版主程序。",
    "重要性": "可以kill"
    },
    "Code.exe": {
    "进程名": "Code.exe",
    "进程描述": "Visual Studio Code 编辑器主程序。",
    "重要性": "可以kill"
    },
    "idea64.exe": {
    "进程名": "idea64.exe",
    "进程描述": "IntelliJ IDEA 开发工具主程序。",
    "重要性": "可以kill"
    },
    "node.exe": {
    "进程名": "node.exe",
    "进程描述": "Node.js JavaScript 运行时环境，通常由开发工具或后台服务启动。",
    "重要性": "可以kill"
    },
    "java.exe / javaw.exe": {
    "进程名": "java.exe / javaw.exe",
    "进程描述": "Java 运行时环境，用于运行 Java 应用程序（如 Minecraft、BurpSuite 等）。",
    "重要性": "可以kill"
    },
    "RtkAudioService64.exe": {
    "进程名": "RtkAudioService64.exe",
    "进程描述": "Realtek 音频服务。负责计算机的声音输出。结束它可能导致没声音。",
    "重要性": "不建议kill"
    },
    "NVIDIA Web Helper.exe": {
    "进程名": "NVIDIA Web Helper.exe",
    "进程描述": "NVIDIA 显卡驱动组件，通常由 GeForce Experience 使用。",
    "重要性": "可以kill"
    },
    "steam.exe": {
    "进程名": "steam.exe",
    "进程描述": "Steam 游戏平台客户端。",
    "重要性": "可以kill"
    },
    "steamwebhelper.exe": {
    "进程名": "steamwebhelper.exe",
    "进程描述": "Steam 的内置浏览器组件，用于显示商店和社区页面。",
    "重要性": "可以kill"
    },
    "OfficeClickToRun.exe": {
    "进程名": "OfficeClickToRun.exe",
    "进程描述": "Microsoft Office 即点即用服务。负责 Office 更新和后台维护。",
    "重要性": "不建议kill"
    },
    "WINWORD.EXE": {
    "进程名": "WINWORD.EXE",
    "进程描述": "Microsoft Word 主程序。",
    },
    "EXCEL.EXE": {
    "进程名": "EXCEL.EXE",
    "进程描述": "Microsoft Excel 主程序。",
    
    },
    "taskhostw.exe": {
    "进程名": "taskhostw.exe",
    "进程描述": "Windows 任务宿主进程。作为 DLL 格式进程的宿主，类似于 svchost 但用于用户任务。"
    },
    "conhost.exe": {
    "进程名": "conhost.exe",
    "进程描述": "控制台窗口主机。为命令行程序（cmd, powershell）提供窗口支持。"
    },
    "Registry": {
    "进程名": "Registry",
    "进程描述": "系统注册表进程，用于加载和缓存注册表数据（在较新版本的 Windows 10/11 中出现）。"
    }
}
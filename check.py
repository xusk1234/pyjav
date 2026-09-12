import winreg

def cj21():
    """Windows 下从注册表查询已安装的 JDK"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\JavaSoft\JDK"
        )
        # 遍历所有子键(即版本号)
        i = 0
        versions = []
        while True:
            try:
                subkey_name = winreg.EnumKey(key, i)
                versions.append(subkey_name)
                i += 1
            except OSError:
                break
        
        print("已安装的 JDK 版本:", versions)
        if any(v.startswith("21") for v in versions):
            print("✅ 检测到 JDK 21")
            return True
        else:
            print("❌ 未检测到 JDK 21")
            return False
    except FileNotFoundError:
        print("❌ 注册表中未找到 JDK")
        return False
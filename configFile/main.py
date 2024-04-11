import configparser

def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def main():
    config = read_config('config.ini')

    # 获取配置项
    database_url = config.get('settings', 'database_url')
    database_port = config.get('settings', 'database_port')
    username = config.get('settings', 'username')
    password = config.get('settings', 'password')

    # 打印配置项
    print(f"Database URL: {database_url}")
    print(f"Database Port: {database_port}")
    print(f"Username: {username}")
    print(f"Password: {password}")

if __name__ == "__main__":
    main()

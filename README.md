# Anthinker

一个简单的网站自动登录和签到工具。

## 功能

- 自动登录
- 自动签到
- 配置文件管理
- 日志记录

## 安装

```bash
git clone https://github.com/WildboarG/anthinker.git
cd anthinker
pip install -r requirements.txt
```

## 使用方法

1. 复制配置文件：
```bash
cp config.json config_test.json
```

2. 修改 `config_test.json`，填入账号密码：
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

3. 运行程序：
```bash
python anthinker.py
```

## 注意事项


- 仅供学习使用，请勿用于非法用途

## 许可证

MIT License
# 部署指南

## Railway 部署步骤

### 1. 准备工作

确保代码已推送到Git仓库：
- Gitee: https://gitee.com/mscfaith/qx-portal-backend

### 2. 在Railway上部署

1. 访问 https://railway.app/
2. 使用GitHub/GitLab账号登录（或创建新账号）
3. 点击 "New Project"
4. 选择 "Deploy from GitHub repo" 或 "Deploy from repo"
5. 如果选择GitHub，需要先导入Gitee仓库到GitHub；或者选择 "Deploy from Git" 输入Gitee仓库URL
   - Gitee URL: `https://gitee.com/mscfaith/qx-portal-backend.git`
6. Railway会自动检测Python项目并开始构建

### 3. 配置环境变量（可选）

在Railway项目设置中添加环境变量：
- `DATABASE_URL`: PostgreSQL连接字符串（如果使用PostgreSQL）
- `ALLOWED_ORIGINS`: 允许的跨域来源（已在代码中配置）

### 4. 初始化数据库

部署完成后，在Railway的终端中运行：
```bash
python init_data.py
```

### 5. 获取部署URL

部署完成后，Railway会提供一个公开URL，类似：
- `https://qx-portal-backend-production.up.railway.app`

### 6. 更新前端配置

将获取到的Railway URL配置到Vercel环境变量中：

```bash
npx vercel env add VITE_API_URL production
# 输入: https://your-railway-url.railway.app
```

然后重新部署前端：
```bash
npx vercel --prod
```

## 替代方案：Render

如果Railway有问题，可以使用Render：

1. 访问 https://render.com/
2. 创建账号并登录
3. 点击 "New +" → "Web Service"
4. 连接Gitee仓库（需要先导入到GitHub）
5. 配置：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. 点击 "Create Web Service"

## 注意事项

- SQLite数据库在每次重新部署时会被清空，生产环境建议使用PostgreSQL
- 确保在生产环境中运行 `python init_data.py` 初始化数据
- 可以在Railway/Render上添加PostgreSQL插件

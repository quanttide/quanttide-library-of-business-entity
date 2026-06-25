# PostHog 参考

## 概述

PostHog 是一个开源产品分析平台，提供事件追踪、会话录制、特征开关、A/B 测试、热力图等功能。

## 部署方式

### PostHog Cloud

SaaS 版本，直接注册使用：https://app.posthog.com

### 自托管

```bash
# 使用 Docker 部署
git clone https://github.com/PostHog/posthog.git
cd posthog

# 启动（含 Postgres、Redis、Celery）
docker compose -f docker-compose.yml up -d
```

## 核心概念

| 概念 | 说明 |
|------|------|
| Event | 用户行为事件（如 pageview、button_click） |
| Person | 用户（匿名或已识别），通过 distinct_id 关联 |
| Action | 事件的聚合规则（如"用户注册"= signup 事件） |
| Cohort | 用户分组（如"过去 7 天活跃用户"） |
| Dashboard | 仪表盘，组合多个图表的看板 |
| Feature Flag | 特征开关，按用户/属性控制功能可见性 |
| Session Recording | 会话录制，回放用户操作轨迹 |

## SDK 接入

### JavaScript / TypeScript

```bash
npm install posthog-js
```

```typescript
import posthog from 'posthog-js'

posthog.init('<PROJECT_API_KEY>', {
  api_host: 'https://app.posthog.com', // 自托管时改为自己的地址
})

// 发送事件
posthog.capture('project_created', { name: '价格指数' })

// 注册用户
posthog.identify('user_123', { email: 'user@example.com' })
```

### Python

```bash
pip install posthog
```

```python
import posthog

posthog.project_api_key = '<PROJECT_API_KEY>'
posthog.host = 'https://app.posthog.com'

posthog.capture('user_123', 'task_completed', {
    'task_type': 'data_cleaning',
    'duration': 3600,
})
```

## 关键功能

### 事件自动采集（可选）

PostHog 默认自动采集 pageview、click、rageclick 等事件，也可通过配置关闭：

```typescript
posthog.init('<KEY>', {
  autocapture: false,        // 关闭自动采集
  capture_pageview: false,   // 关闭页面浏览采集
})
```

### Session Recording

录制用户会话，回放鼠标移动、点击、滚动、输入：

```typescript
posthog.init('<KEY>', {
  session_recording: {
    mask_all_text: true,             // 屏蔽文本内容
    mask_all_element_attributes: true, // 屏蔽元素属性
  },
})
```

### Feature Flags

```typescript
// 判断用户是否有某特征
if (posthog.isFeatureEnabled('new-dashboard')) {
  renderNewDashboard()
} else {
  renderOldDashboard()
}
```

### 上报数据类型的约定

| Payload 字段 | 必填 | 说明 |
|-------------|------|------|
| `distinct_id` | 是 | 用户唯一标识 |
| `event` | 是 | 事件名称（snake_case 约定） |
| `properties` | 否 | 事件属性（同级属性打平，不要嵌套） |
| `timestamp` | 否 | 默认取服务器时间 |

## 自托管系统要求

| 组件 | 建议配置 |
|------|---------|
| CPU | 2 核以上 |
| 内存 | 8 GB 以上 |
| 存储 | 50 GB SSD（取决于数据量） |
| 依赖 | Postgres、Redis、Celery（可选） |

## 参考链接

- 官方文档：https://posthog.com/docs
- GitHub：https://github.com/PostHog/posthog
- 定价：https://posthog.com/pricing

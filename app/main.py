from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from .database import engine, Base
from .routers import content, banners, features

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="QX Portal API",
    description="Backend API for QX Portal - Advertising and Content Marketing Platform",
    version="1.0.0"
)

# CORS middleware
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000,https://qx-portal.vercel.app").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins + ["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(content.router)
app.include_router(banners.router)
app.include_router(features.router)

# Create upload directory
os.makedirs("uploads", exist_ok=True)

# Mount static files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def root():
    return {
        "message": "QX Portal API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/init-db")
def initialize_database():
    """Initialize database with sample data (use once for initial setup)"""
    from .database import SessionLocal
    from . import models

    db = SessionLocal()

    try:
        # Check if data already exists
        existing_banners = db.query(models.Banner).count()
        if existing_banners > 0:
            return {
                "status": "skipped",
                "message": "Database already initialized",
                "counts": {
                    "banners": db.query(models.Banner).count(),
                    "content_items": db.query(models.ContentItem).count(),
                    "features": db.query(models.Feature).count()
                }
            }

        # Sample Banners
        banners = [
            models.Banner(
                title="让您的品牌",
                subtitle="触达亿万用户",
                description="专业的广告投放与内容运营服务，助力企业快速增长。精准触达目标用户，提升品牌影响力。",
                badge="领先的广告推广平台",
                button1_text="立即开始",
                button2_text="观看演示",
                stat1_value="1,000+",
                stat1_label="合作企业",
                stat2_value="50M+",
                stat2_label="覆盖用户",
                stat3_value="98%",
                stat3_label="客户满意度",
                image_url="",
                order=1,
                status=True
            )
        ]

        # Sample Content Items
        content_items = [
            models.ContentItem(
                title="2026年度营销趋势报告",
                description="深入分析行业最新动态，把握市场机遇，制定精准营销策略",
                cover="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80",
                category="行业洞察",
                views="12.5K",
                likes="1.2K",
                comments="234",
                author="营销专家",
                order=1,
                status=True
            ),
            models.ContentItem(
                title="如何打造爆款短视频内容",
                description="从创意策划到数据分析，全方位提升内容质量与传播效果",
                cover="https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=600&q=80",
                category="内容创作",
                views="28.3K",
                likes="3.5K",
                comments="567",
                author="内容总监",
                order=2,
                status=True
            ),
            models.ContentItem(
                title="精准投放：广告效果提升300%",
                description="数据驱动的投放策略，让每一次曝光都触达精准用户群体",
                cover="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80",
                category="投放技巧",
                views="45.7K",
                likes="6.8K",
                comments="892",
                author="投放专家",
                order=3,
                status=True
            ),
            models.ContentItem(
                title="社交媒体运营完整指南",
                description="多平台运营策略，提升品牌影响力，建立用户粘性",
                cover="https://images.unsplash.com/photo-1611926653458-09294b3142bf?w=600&q=80",
                category="社媒运营",
                views="19.2K",
                likes="2.4K",
                comments="345",
                author="运营经理",
                order=4,
                status=True
            ),
            models.ContentItem(
                title="品牌出海营销策略解析",
                description="跨境营销的关键要素，助力品牌成功拓展国际市场",
                cover="https://images.unsplash.com/photo-1557804506-669a67965ba0?w=600&q=80",
                category="出海营销",
                views="32.1K",
                likes="4.2K",
                comments="678",
                author="出海顾问",
                order=5,
                status=True
            ),
            models.ContentItem(
                title="AI赋能内容创作新时代",
                description="探索人工智能如何革新内容生产，提升创作效率和质量",
                cover="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&q=80",
                category="AI技术",
                views="56.8K",
                likes="8.9K",
                comments="1.2K",
                author="技术专家",
                order=6,
                status=True
            ),
        ]

        # Sample Features
        features = [
            models.Feature(
                title="极速投放",
                description="智能化投放系统，5分钟完成广告上线，实时监控投放效果",
                icon="ThunderboltFilled",
                gradient="from-yellow-400 to-orange-500",
                order=1,
                status=True
            ),
            models.Feature(
                title="数据驱动",
                description="全方位数据分析，精准洞察用户行为，优化投放策略",
                icon="BarChartOutlined",
                gradient="from-green-400 to-emerald-500",
                order=2,
                status=True
            ),
            models.Feature(
                title="精准触达",
                description="智能人群画像，多维度定向投放，提升转化率300%",
                icon="TeamOutlined",
                gradient="from-purple-400 to-pink-500",
                order=3,
                status=True
            ),
            models.Feature(
                title="安全可靠",
                description="企业级安全保障，数据加密传输，保护品牌与用户隐私",
                icon="SafetyOutlined",
                gradient="from-blue-400 to-cyan-500",
                order=4,
                status=True
            ),
            models.Feature(
                title="全域覆盖",
                description="覆盖主流媒体平台，一站式管理，扩大品牌影响力",
                icon="GlobalOutlined",
                gradient="from-indigo-400 to-blue-500",
                order=5,
                status=True
            ),
            models.Feature(
                title="专业服务",
                description="7×24小时专属客服，资深运营团队全程指导",
                icon="CustomerServiceOutlined",
                gradient="from-rose-400 to-red-500",
                order=6,
                status=True
            ),
        ]

        # Add all data
        db.add_all(banners)
        db.add_all(content_items)
        db.add_all(features)
        db.commit()

        return {
            "status": "success",
            "message": "Database initialized successfully",
            "counts": {
                "banners": len(banners),
                "content_items": len(content_items),
                "features": len(features)
            }
        }

    except Exception as e:
        db.rollback()
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        db.close()

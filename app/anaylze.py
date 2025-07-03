# python lib

# 3rd party lib
from fastapi import APIRouter, Query, Body, Header, Depends
from sqlalchemy.orm import Session

# internal project lib
import app.models as table
import app.task as task

from app import schemas
from app.models import AnalysisStatusEnum
from app.gplay import fetch_reviews, fetch_app_detail
from app.config.database import get_db
from app.helper.network import success_response, error_response

router = APIRouter()

@router.post("/analyses")
def post_analyses(db: Session = Depends(get_db), payload: schemas.PostAnalyzeRequest = None):
    analysis_id = payload.analysis_id
    application_id = payload.application_id
    
    application = db.query(table.Application).filter(table.Application.application_id == application_id).first()
    
    if application is None:
        # Checking status analysis
        if analysis_id is not None:
            analysis = db.query(table.Analysis).filter(table.Analysis.analysis_id == analysis_id).first()
            
            if analysis is not None:
                return success_response({
                    "analysis_id":  analysis_id,
                    "application_id": application_id,
                    "status": analysis.status
                })
        
        # New Analysis    
        if analysis_id is None:
            # Insert Application
            res_app_detail = fetch_app_detail(application_id)
            new_app = table.Application(**res_app_detail)
            
            db.add(new_app)
            db.flush() # <-- db insert (uncommited)
            
            # Insert Analyses
            new_analysis = table.Analysis(application_id=application_id)
            db.add(new_analysis)
            db.flush()
            db.refresh(new_analysis)
            
            analysis_id = new_analysis.analysis_id
                
        # Do Scraping
        reviews, string_token = fetch_reviews(app_id=payload.application_id, count=2)
        
        worker = task.do_sentiment_analyses.delay(reviews)
        
        
        
        # db.commit()
        return success_response({
                    "analysis_id":  analysis_id,
                    "application_id": application_id,
                    "status": AnalysisStatusEnum.PROCESSING,
                    "task_id": worker.id
                })
        
    else:
        print("select anlysis limit 2000")
        
        return success_response({
                    "analysis_id":  analysis_id,
                    "application_id": application_id,
                    "status": AnalysisStatusEnum.PROCESSING
                })
        
        

@router.post("/v2/analyses")
def post_analyses(db: Session = Depends(get_db), payload: schemas.PostAnalyzeRequest = None):
    analysis_id = payload.analysis_id
    application_id = payload.application_id
    
    application = db.query(table.Application).filter(table.Application.application_id == application_id).first()
    
    if application is None:
        # Checking status analysis
        if analysis_id is not None:
            analysis = db.query(table.Analysis).filter(table.Analysis.analysis_id == analysis_id).first()
            
            if analysis is not None and analysis.status != AnalysisStatusEnum.PROCESSING:
                return success_response({
                    "analysis_id":  analysis_id,
                    "application_id": application_id,
                    "status": AnalysisStatusEnum.COMPLETED
                })
        
        # New Analysis    
        if analysis_id is None:
            # Insert Application
            res_app_detail = fetch_app_detail(application_id)
            new_app = table.Application(**res_app_detail)
            
            db.add(new_app)
            db.flush() # <-- db insert (uncommited)
            
            # Insert Analyses
            new_analysis = table.Analysis(application_id=application_id)
            db.add(new_analysis)
            db.flush()
            db.refresh(new_analysis)
            
            analysis_id = new_analysis.analysis_id
                
        # Do Scraping
        reviews, string_token = fetch_reviews(app_id=payload.application_id, count=2)
        
        worker = task.do_sentiment_analyses.delay(reviews)
        
        
        
        # db.commit()
        return success_response({
                    "analysis_id":  analysis_id,
                    "application_id": application_id,
                    "status": AnalysisStatusEnum.PROCESSING,
                    "task_id": worker.id
                })
        
    else:
        print("select anlysis limit 2000")
        
        return success_response({
                    "analysis_id":  analysis_id,
                    "application_id": application_id,
                    "status": AnalysisStatusEnum.PROCESSING
                })
from typing import List
import logging
from steam_content_based_recsys import SteamContentBasedRecSys, ContentBasedRecommendation
from app.models.schemas import RecommendationRequest, RecommendationItem


logger = logging.getLogger(__name__)


recsys_v1 = SteamContentBasedRecSys().load(index_path='data/recsys-v1.index', idx2id_path='data/idx2id.json')
recsys_v2 = SteamContentBasedRecSys().load(index_path='data/recsys-v2.index', idx2id_path='data/idx2id.json')


class RecsysService:
    def recommend(self, request: RecommendationRequest, recsys_version: str = 'v1') -> List[RecommendationItem]:
        recommendations: list[ContentBasedRecommendation] = []

        logger.info("Начало формирования рекомендаций")

        if recsys_version == 'v1':
            recommendations = recsys_v1.recommend(request.liked_games_ids, request.m)
        else:
            recommendations = recsys_v2.recommend(request.liked_games_ids, request.m)
        
        result: List[RecommendationItem] = []
        for rec_sample in recommendations:
            result.append(RecommendationItem(rec=rec_sample.recommendation, src=rec_sample.original))

        logger.info("Рекомендации успешно получены")

        return result
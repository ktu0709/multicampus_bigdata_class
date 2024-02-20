from django.apps import AppConfig
import joblib

class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"

class loadmodel(AppConfig):
    name = 'polls'
    verbose_name = '스펙 입력하고 기업 예측하기'

    def ready(self):

        self.model = joblib.load('polls/model/train_model.joblib')
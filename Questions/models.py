from tabnanny import verbose
from django.db import models

# Question, Score, and Answer models are created here.

class Question(models.Model):
    question_text = models.TextField(max_length=250)

    class Meta:
        db_table = 'question'
        verbose_name = 'Question'
        verbose_name_plural = 'questions'
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'answer'
        verbose_name = 'Answer'
        verbose_name_plural = 'answers'

    def __str__(self):
        return self.answer_text


class Score(models.Model):
    score_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.score_number)
    
    def update_score(self, answer):
        if answer.is_correct:
            self.score_number += 5
            self.save()
        else:
            self.score_number -= 5
            self.save()


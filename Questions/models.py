from django.db import models

# Question, Score, and Answer models are created here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Score(models.Model):
    score_number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score_number)
    
    def update_score(self, answer):
        if answer.is_correct:
            self.score_number += 5
            self.save()
        else:
            self.score_number -= 5
            self.save()


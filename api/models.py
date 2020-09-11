from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название группы')
    description = models.TextField(verbose_name='Описание группы')

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='posts',
                              verbose_name='Группа')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="comments")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления",
                                   auto_now_add=True,
                                   db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False, related_name='follower',
                             verbose_name='Подписчик')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  null=False, related_name='following',
                                  verbose_name='Авторы на которых подписан')

    class Meta:
        unique_together = ['user', 'following']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

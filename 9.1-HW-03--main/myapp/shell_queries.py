# shell_queries.py
# Примеры запросов к моделям Django для приложения myapp

# Чтобы использовать эти запросы, выполните в терминале:
# python manage.py shell
# Затем скопируйте и вставьте нужные запросы или импортируйте этот файл:
# from shell_queries import *

from myapp.models import Author, Category, Post, Comment, PostCategory
from django.contrib.auth.models import User

# 1. Создание объектов

# Создание пользователя
user1 = User.objects.create_user(username='user1', password='password1')
user2 = User.objects.create_user(username='user2', password='password2')

# Создание авторов
author1 = Author.objects.create(user=user1, rating=0)
author2 = Author.objects.create(user=user2, rating=0)

# Создание категорий
category1 = Category.objects.create(name='Политика')
category2 = Category.objects.create(name='Технологии')
category3 = Category.objects.create(name='Спорт')
category4 = Category.objects.create(name='Культура')

# Создание постов
post1 = Post.objects.create(
    author=author1,
    post_type='AR',
    title='Новая политическая реформа',
    text='Текст статьи о политической реформе...',
    rating=5
)
post1.categories.add(category1, category2)

post2 = Post.objects.create(
    author=author2,
    post_type='NW',
    title='Новости технологий',
    text='Последние новости из мира технологий...',
    rating=8
)
post2.categories.add(category2)

post3 = Post.objects.create(
    author=author1,
    post_type='AR',
    title='Спортивные достижения',
    text='Обзор последних спортивных событий...',
    rating=3
)
post3.categories.add(category3)

# Создание комментариев
comment1 = Comment.objects.create(post=post1, user=user2, text='Интересная статья!', rating=2)
comment2 = Comment.objects.create(post=post2, user=user1, text='Спасибо за новости!', rating=4)
comment3 = Comment.objects.create(post=post1, user=user1, text='Не согласен с автором', rating=0)
comment4 = Comment.objects.create(post=post3, user=user2, text='Отличный обзор!', rating=1)

# 2. Основные запросы

# Все авторы
all_authors = Author.objects.all()

# Все категории
all_categories = Category.objects.all()

# Все посты
all_posts = Post.objects.all()

# Все комментарии
all_comments = Comment.objects.all()

# 3. Фильтрация

# Посты определенного автора
author_posts = Post.objects.filter(author=author1)

# Статьи (не новости)
articles = Post.objects.filter(post_type='AR')

# Новости
news = Post.objects.filter(post_type='NW')

# Посты с рейтингом больше 5
top_posts = Post.objects.filter(rating__gt=5)

# Комментарии к определенному посту
post_comments = Comment.objects.filter(post=post1)

# Комментарии определенного пользователя
user_comments = Comment.objects.filter(user=user1)

# 4. Сортировка

# Посты, отсортированные по рейтингу (по убыванию)
posts_by_rating = Post.objects.order_by('-rating')

# Комментарии, отсортированные по дате создания (новые сначала)
comments_by_date = Comment.objects.order_by('-created_at')

# 5. Обновление рейтингов

# Лайк посту
post1.like()  # увеличит рейтинг на 1
post2.like()

# Дизлайк посту
post3.dislike()  # уменьшит рейтинг на 1

# Лайк комментарию
comment1.like()
comment2.like()

# Дизлайк комментарию
comment3.dislike()

# 6. Обновление рейтинга автора
author1.update_rating()
author2.update_rating()

# Проверка обновленного рейтинга
updated_author1 = Author.objects.get(pk=author1.pk)
updated_author2 = Author.objects.get(pk=author2.pk)

# 7. Вывод информации

# Лучший пост (по рейтингу)
best_post = Post.objects.order_by('-rating').first()

# Вывод информации о посте
if best_post:
    print(f"Лучший пост: {best_post.title}")
    print(f"Автор: {best_post.author.user.username}")
    print(f"Превью: {best_post.preview()}")
    print(f"Рейтинг: {best_post.rating}")
    print("Категории:", ", ".join([cat.name for cat in best_post.categories.all()]))

# 8. Удаление объектов

# Удаление комментария
# comment1.delete()

# Удаление поста
# post3.delete()

# 9. Примеры сложных запросов

# Посты в категории "Технологии"
tech_posts = Post.objects.filter(categories__name='Технологии')

# Авторы, у которых есть посты с рейтингом больше 5
top_authors = Author.objects.filter(post__rating__gt=5).distinct()

# Комментарии к постам определенного автора
author_comments = Comment.objects.filter(post__author=author1)

# 10. Работа с ManyToMany

# Добавление категории к посту
post1.categories.add(category4)

# Удаление категории у поста
post1.categories.remove(category2)

# Все категории поста
post1_categories = post1.categories.all()

# Все посты в категории
category_posts = category1.post_set.all()

print("\nПримеры запросов готовы к использованию!")
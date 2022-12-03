from news.models import *

# 1

u1 = User.objects.create_user(username = 'Artyom')
u2 = User.objects.create_user(username = 'Viktor')

# 2

a1 = Author.objects.create(userAuthor = u1)
a2 = Author.objects.create(userAuthor = u2)

# 3

c1 = Category.objects.create(title = 'IT')
c2 = Category.objects.create(title = 'Gaming')
c3 = Category.objects.create(title = 'Agricultural industry')
c4 = Category.objects.create(title = 'Space')

# 4

pa1 = Post.objects.create(author = a1, category_type = 'AR', header = 'Space technologies', text = 'Something about space and technologies')
pa2 = Post.objects.create(author = a2, category_type = 'AR', header = 'Space games', text = 'All about space in games')
pn1 = Post.objects.create(author = a2, category_type = 'NW', header = 'How does Farming in Games Affect Nature?', text = 'Does not affect in any way')

# 5

add1 = pa1.categories.add(c1,c4)
add2 = pa2.categories.add(c2,c4)
add3 = pn1.categories.add(c2,c3)

# 6

com1 = Comment.objects.create(post_com = pa1, user_com = a2.userAuthor, text = 'The author wrote a boring article')
com2 = Comment.objects.create(post_com = pa1, user_com = a2.userAuthor, text = 'Check my article and news')
com3 = Comment.objects.create(post_com = pa2, user_com = a1.userAuthor, text = 'Your article so interesting')
com4 = Comment.objects.create(post_com = pn1, user_com = a1.userAuthor, text = 'Your news is so funny')

# 7

pa1.like()
pa1.like()
pa1.like()
pa1.like()
pa1.like()
pa1.dislike()
pa2.dislike()
pa2.dislike()
pa2.like()
pn1.like()
pn1.like()
pn1.like()
pn1.dislike()

com1.dislike()
com2.dislike()
com1.dislike()
com3.like()
com3.like()
com3.dislike()
com3.like()
com4.like()
com4.dislike()
com4.like()
com4.like()
com3.like()

# 8

a1.update_rating()
a2.update_rating()

# 9

best_au = Author.objects.order_by('-rating')[0]
best_au.userAuthor.username
best_au.rating

# 10

best_po = Post.objects.order_by('-rating')[0]
best_po.time
best_po.author.userAuthor.username
best_po.rating
best_po.header
best_po.preview()

# 11

compo = Comment.objects.filter(post_com = best_po.id)
for item in compo:
     item.time
     item.user_com
     item.rating
     item.text
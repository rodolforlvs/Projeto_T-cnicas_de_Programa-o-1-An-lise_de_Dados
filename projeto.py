import pandas as pd

business = pd.read_csv('courses_business.csv')
design = pd.read_csv('courses_design.csv')
music = pd.read_csv('courses_music.csv')
web_dev = pd.read_csv('courses_web_development.csv')

db = pd.concat([business, design, music, web_dev])
db

# #1 - Quantos cursos estão disponíveis na plataforma?
print('Estão disponíveis na plataforma', db['course_title'].count(),'cursos')
#############################################################
# #2 Quais e quantos são os cursos que abordam o assunto: JavaScript?
db['course_title'] = db['course_title'].str.lower()
javascript = db[db['course_title'].str.contains('javascript', na= False)]
total_javascript = len(javascript)
print(total_javascript, 'cursos, abordam o assunto: JavaScript')
#############################################################
#3 - Qual é o preço médio (coluna price) dos cursos oferecidos na plataforma?
df = pd.DataFrame(db)
mean_df = df['price'].mean()
print(f'Preço médio dos cursos R$ {mean_df:.2f}')
#############################################################
#4 - Quais são os cinco cursos com maior número de inscritos (coluna num_subscribers)?
maior_inscritos = db.groupby('course_title').max().reset_index()[
    ['course_title',
     'num_subscribers']
].sort_values('num_subscribers', ascending=False).head(5)

print(f'Estes são os 5 cursos com maior número de inscritos:\n{maior_inscritos}')
#############################################################
#5 - Dos cinco cursos mais populares em termos de inscritos, mostre o rate médio, máximo e mínimo de cada um deles.
rates = db.groupby('course_title').max().reset_index()[
    ['course_title',
     'num_subscribers', 'Rating']
].sort_values('num_subscribers', ascending=False).head(5)

rates.describe()
descricao = rates.describe()
print(f'A descrição dos 5 cursos mais populares:\n{descricao}')
#############################################################
# 6 - Apresente os dez cursos mais avaliações na plataforma.
avaliacoes = db.sort_values(by='num_reviews', ascending=False).reset_index().head(10)
print(f'os dez cursos mais avaliados\n{avaliacoes}')

#7 - A partir dos dez cursos mais avaliações, mostre:
# 1. Qual tem o maior número de inscritos;
inscritos = avaliacoes.sort_values(by='num_subscribers', ascending=False).reset_index()
maior = [inscritos['course_title'][0]]
inscritos = avaliacoes['num_subscribers'].max()
print(f'Curso com mais inscrições é {maior}.\nPossui: {inscritos} inscritos')
# 2. Qual tem o maior rate (avaliação do curso).
rate = avaliacoes.sort_values(by='Rating', ascending=False).reset_index()
maior_rate = [rate['course_title'][0]]
rate = avaliacoes['Rating'].max()
print(f'Curso melhor avaliado é {maior_rate}.\nPossui nota: {rate}')

# 8 - Dos cursos listados na base de dados, qual tem maior duração em horas?
dh = db.sort_values(by='content_duration', ascending=False).reset_index()
curso_maior_dh = dh['course_title'][0]
maior_dh = dh['content_duration'][0]
print(f'O curso: {curso_maior_dh} \nTem duração de {maior_dh} horas')

#9 - Dos cursos listados na base de dados, qual tem o maior número de aulas (lectures)?
maior_num_aulas = db['num_lectures'].max()
curso_maior = db[db['num_lectures'] == maior_num_aulas]
print(curso_maior)

#10 - Apresente o número (contagem) de cursos agrupados por nível (coluna level).

agrupados = db.groupby(by='level').count().reset_index()
print(agrupados)

#11 - Quais são os cursos mais recentes contidos na base de dados?
recentes = db.sort_values(by='published_timestamp', ascending=False).reset_index()
mais_recentes = recentes.head()
print(f'Cursos mais recentes: \n{mais_recentes}')

#12 - Apresente o número (contagem) de cursos agrupados por nível (coluna level) e por assunto (coluna subject).
agrp_nivel= db.groupby(by=['level', 'subject']).count().reset_index()
print(f'Cursos agrupados por nível e por assunto:\n{agrp_nivel}')
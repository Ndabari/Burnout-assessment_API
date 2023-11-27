from models.questions import Questions
from utils.db_conn import Base, session, engine

Base.metadata.create_all(engine)

q_1 = Questions('D1', 'Do you find yourself less interested in your classes or academic activities than before')
q_2 = Questions('D2', 'Have you noticed a decline in your enthusiasm for learning')
q_3 = Questions('D3', 'Do you tend to need more time than before to complete your '
                      'academic assignments or prepare for exams')
q_4 = Questions('D4', 'Have you found it challenging to balance your academic workload with other aspects of your life')
q_5 = Questions('D5', 'Do you find yourself avoiding interactions with classmates '
                      'or participating less in group activities')
q_6 = Questions('D6', 'Have you noticed a decrease in your social engagement related to academic events or discussions')
q_7 = Questions('D7', 'Have you noticed any changes in your social interactions or withdrawal from social activities?')
q_8 = Questions('D8', 'Do you question the relevance of what you\'re studying to your future goals?')
q_9 = Questions('D9', 'Have you found it challenging to see the practical application of your academic work?')
q_10 = Questions('E1', 'Have you experienced a lack of excitement or passion about your academic pursuits?')
q_11 = Questions('E2', 'Have you experienced a decrease in motivation or a sense of apathy toward your academic goals?')
q_12 = Questions('E3', 'Do you feel emotionally disconnected or indifferent toward your coursework?')
q_13 = Questions('E4', 'Do you often feel mentally exhausted or overwhelmed by the demands of your coursework?')
q_14 = Questions('E5', 'Have you experienced difficulties concentrating or focusing on your studies?')
q_15 = Questions('E6', 'Have you noticed an increase in feelings of stress, '
                       'anxiety, or frustration related to your academic responsibilities?')
q_16 = Questions('E7', 'Do you find that your studies are emotionally draining, '
                       'leaving you feeling emotionally exhausted?')
q_17 = Questions('E8', 'Are you able to engage in activities you enjoy outside of school?')
q_18 = Questions('E9', 'Do you struggle to find meaning or purpose in your academic pursuits?')

session.add(q_1)
session.add(q_2)
session.add(q_3)
session.add(q_4)
session.add(q_5)
session.add(q_6)
session.add(q_7)
session.add(q_8)
session.add(q_9)
session.add(q_10)
session.add(q_11)
session.add(q_12)
session.add(q_13)
session.add(q_14)
session.add(q_15)
session.add(q_16)
session.add(q_17)
session.add(q_18)

session.commit()
session.close()

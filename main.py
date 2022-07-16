import utility as util
import questions as q

util.printGenres(q.questions)
genre = util.getAnswer()

rightAnswers = util.goThroughQuestions(q.questions, genre)
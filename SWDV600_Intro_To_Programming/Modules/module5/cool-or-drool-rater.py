# cool-or-drool-rater.py
#
# This program generates overall movie ratings based on multiple
#   individual movie ratings

import graphics as g

def getMovieRatingsFile():
    while True:
        try:
            # get user input of file containing movie ratings (inFileName)
            inFileName = input('Enter the name of the file with the movie ratings: ')

            inFile = open(inFileName, 'r')
            # if the file was opened without error, return the file
            return inFileName, inFile
        except FileNotFoundError:
            print('"{0}" was not found'.format(inFileName))
        except:
            print('Uh Oh! There was an error opening the file.')


def main():
    inFileName, inFile = getMovieRatingsFile()
    
    # get the movie title
    firstLine = inFile.readline()
    firstLineTokens = firstLine.strip().split(',')
    movieTitle = firstLineTokens[1]
    
    # initialize accumulation variables
    totalNumberOfRatings = 0
    ratingsTotal = 0 # the sum of each individual rating
    sixOrHigher = 0 # the total number of ratings that is >= 6
    
    nextLine = inFile.readline()
    sentinal = ''

    # loop through each line of the file
    while nextLine != sentinal:
        # strip and split the line on ','
        ratingsSeq = nextLine.strip().split(',')
        totalNumberOfRatings = totalNumberOfRatings + len(ratingsSeq)
        for rating in ratingsSeq:
            rating = int(rating)
            ratingsTotal = ratingsTotal + rating
            if rating >= 6:
                sixOrHigher +=  1
            
        nextLine = inFile.readline()
    
    # calculate the cool percentage
    coolPct = sixOrHigher/totalNumberOfRatings

    # calculate average rating (avgRating)
    avgRating = ratingsTotal / totalNumberOfRatings

    # calculate (ratingPercent) avgRating / 10
    ratingPercent = avgRating / 10

    # initialize movieRating
    movieRating = None
    if totalNumberOfRatings < 10:
        movieRating = 'TOO SOON TO RULE'
        imageName = 'toosoontorule'
    elif coolPct >= 0.6:
        movieRating = 'COOL'
        imageName = 'cool'
    else:
        movieRating = 'DROOL'
        imageName = 'drool'
    
    # close the inFile
    inFile.close()
    
    print()
    print('Movie Title:', movieTitle)
    print('Total Number of Ratings:', totalNumberOfRatings)
    print('Cool Percentage:', coolPct)
    print('Certified', movieRating)

    # create graphics window 400 x 400
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400
    win = g.GraphWin('Is this movie COOL or DROOL?', WINDOW_WIDTH, WINDOW_HEIGHT)

    # draw the title of the movie in the top center
    title = g.Text(g.Point(WINDOW_WIDTH/2, 40), movieTitle)
    title.draw(win)

    # draw the corresponding movieRating image
    imagePath = 'movie_ratings_gifs/{}.gif'.format(imageName)
    image = g.Image(g.Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2), imagePath)
    image.draw(win)

    # draw the ratingPercent and movieRating at bottom center
    movieRtgText = '{0:0.0f}% {1}'.format(coolPct * 100, movieRating.lower())
    ratingPct = g.Text(g.Point(WINDOW_WIDTH/2, WINDOW_HEIGHT-40), movieRtgText)
    ratingPct.draw(win)

main()
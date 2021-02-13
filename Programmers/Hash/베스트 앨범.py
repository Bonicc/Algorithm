def solution(genres, plays):
    answer = []
    best_genres = dict()
    best_song_for_each_genres = dict()
    plays = list(enumerate(plays))
    for i in range( len(plays)):
        try:
            best_genres[genres[i]] += plays[i][1]
            best_song_for_each_genres[genres[i]].append(plays[i])
        except:
            best_genres[genres[i]] = plays[i][1]
            best_song_for_each_genres[genres[i]] = []
            best_song_for_each_genres[genres[i]].append(plays[i])
        
    best_genres = list(map(lambda x: x[0], sorted(best_genres.items(), key = lambda x : x[1], reverse = True)))
    
    for i in best_genres:
        sb = sorted(best_song_for_each_genres[i], key = lambda x: x[1],reverse = True)      
        answer.append(sb[0][0])
        if len(sb)>1:
            answer.append(sb[1][0])
                
    return answer
import re

def solution(word, pages):
    word = word.lower()
    dic_url = {}
    for page in pages:
        url = page.split('<meta property="og:url" content="https://')[1].split('"')[0]
        body = page.split('<body>')[1].split('</body>')[0].replace("\n", "").lower()

        find_url = body.split('<a href="https://')
        temp = []
        for i in range(1, len(find_url)):
            link = find_url[i].split('"')[0]
            if link != url:
                temp.append(link)
        
        body = re.findall('[a-zA-Z]+', body)
        score = 0
        for s in body:
            if s == word:
                score += 1
                
        dic_url[url] = [score, temp, 0]

    for value in dic_url.values():
        score = value[0] / len(value[1])
        for link in value[1]:
            if link not in dic_url:
                continue
            dic_url[link][2] += score
    
    max_value = max_idx = 0
    idx = 0
    for value in dic_url.values():
        if value[0] + value[2] > max_value:
            max_value = value[0] + value[2]
            max_idx = idx
        idx += 1

    return max_idx

print(solution(	"blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
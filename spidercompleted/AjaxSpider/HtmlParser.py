import re
import json


# 提取当前正在上映的电影链接
class HtmlParser(object):

    def parser_url(self, page_url, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls != None:
            # 将urls进行去重
            return list(set(urls))
        else:
            return None

    def parser_json(self, page_url, response):
        '''
        解析响应
        :param response:
        :return
        '''
        # 将“=”和“；”之间的内容提取出来
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result != None:
            # json模块加载字符串
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print(e)
                return None
            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url, value, isRelease=2)
            else:
                return self._parser_no_release(page_url, value)

    def _parser_release(self, page_url, value):
        '''
        解析已经上映的影片
        :param page_url:电影链接
        :param value:数据
        :return
        '''
        try:
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')
            movieTitle = value.get('value').get('movieTitle')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            TotalBoxOffice = boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice = boxOffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')

            ShowDays = boxOffice.get('ShowDays')
            try:
                Rank = boxOffice.get('Rank')
            except Exception as e:
                Rank = 0
            # 返回所提取的内容
            return (MovieId, movieTitle, RatingFinal, ROtherFinal,
                    RPictureFinal, RDirectorFinal, RStoryFinal, Usercount,
                    AttitudeCount, TotalBoxOffice + TotalBoxOfficeUnit,
                    TodayBoxOffice + TodayBoxOfficeUnit, Rank, ShowDays, isRelease)
        except Exception as e:
            print(e, page_url, value)
            return None

    def _parser_no_release(self, page_url, value, isRelease=0):
        '''
        解析未上映的电影信息
        :param page_url:
        :param value:
        :return
        '''
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')
            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                Rank = 0
            # 返回所提取的内容
            return (MovieId, movieTitle, RatingFinal, ROtherFinal,
                    RPictureFinal, RDirectorFinal, RStoryFinal, Usercount,
                    AttitudeCount, u'无', u'无', Rank, 0, isRelease)
        except Exception as e:
            print(e, page_url, value)
            return None


'''
if __name__ == '__main__':
    parsr = HtmlParser()
    parsr.parser_json('http://theater.mtime.com/China_Beijing/')
'''

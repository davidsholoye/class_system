# from diary_entry_class import DiaryEntry

class Diary:
    def __init__(self):
        self.dict = {}

    def add(self, entry):
        self.dict[entry.title] = entry.contents

    def all(self):
        return self.dict

    def count_words(self):
        value = list(self.dict.values())
        counter = 0
        for i in value:
            counter += len(i.split())
        return counter 

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# diary = Diary()
# diary_entry_1 = DiaryEntry('title1', 'this is day 14 at makers')
# diary.add(diary_entry_1)
# print(diary.count_words())s
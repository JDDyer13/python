class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        '''
        :Method: Change the tv power
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        '''
        :Method: Mute or unmute the tv
        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        '''
        :Method:  Increase tv channel
        '''
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        '''
        :Method: Decrease tv channel
        '''
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        '''
        :Method: Increase tv volume
        '''
        if self.__status == True:
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        if self.__muted == True:
            self.__muted = False

    def volume_down(self):
        '''
        :Method: Decrease tv volume
        '''
        if self.__status == True:
            if self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        if self.__muted == True:
            self.__muted = False

    def __str__(self) -> str:
        '''
        Method to show tv status
        :return: tv status
        '''
        '''
        :return: 
        '''
        if self.__muted == False:
            return (f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}')
        else:
            return (f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0')



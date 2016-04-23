from song import Song

class FurElise(Song):
    def __init__(self):
        super(self.__class__, self).__init__()

    def song_name(self):
        return 'fur_elise'

    def sequences(self):
        return {
            'right_hand': {
                'options': {
                    'seconds_per_bar': 1.35, 
                    'frequency': 1200, 
                    'top_volume': 127.0,
                    'nblacks': 6.0
                },
                'tones':  [('SILENCE', 2),
                     ('SILENCE', 4), ('E5', 1), ('D#5', 1),
                     ('E5', 1), ('D#5', 1), ('E5', 1), ('B4', 1), ('D5', 1), ('C5', 1),
                     ('A4', 3), ('C', 1), ('E', 1), ('A4', 1),
                     ('B4', 3), ('E', 1), ('G#4', 1), ('B4', 1),
                     ('C5', 3), ('E', 1), ('E5', 1), ('D#5', 1),
                     ('E5', 1), ('D#5', 1), ('E5', 1), ('B4', 1), ('D5', 1), ('C5', 1),
                     ('A4', 3), ('C', 1), ('E', 1), ('A4', 1),
                     ('B4', 3), ('E', 1), ('C5', 1), ('B4', 1),
                     ('A4', 3)
                ]
            },
            'left_hand': {
                'options': {
                    'seconds_per_bar': 1.35, 
                    'frequency': 1200, 
                    'top_volume': 127.0,
                    'nblacks': 6.0
                },
                'tones': [('SILENCE', 2),
                        ('SILENCE', 6),
                        ('SILENCE', 6),
                        ('A2', 1), ('E3', 1), ('A3', 1), ('SILENCE', 3),
                        ('C2', 1), ('E3', 1), ('G#3', 1), ('SILENCE', 3),
                        ('E2', 1), ('E3', 1), ('A3', 1), ('SILENCE', 3),
                        ('SILENCE', 6),
                        ('E2', 1), ('E3', 1), ('A3', 1), ('SILENCE', 3),
                        ('C2', 1), ('E3', 1), ('G#3', 1), ('SILENCE', 3),
                        ('E2', 1), ('E3', 1), ('A3', 1)
                ]
            }
        }

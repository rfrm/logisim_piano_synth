from song import Song

class OdeToJoy(Song):
    def __init__(self):
        super(self.__class__, self).__init__()

    def song_name(self):
        return 'ode_to_joy'

    def sequences(self):
        return {
            'right_hand': {
                'options': {
                    'seconds_per_bar': 1.35, 
                    'frequency': 1200, 
                    'top_volume': 127.0,
                    'nblacks': 4.0
                },
                'tones': [('SILENCE', 2),
                     ('E', 1), ('E', 1), ('F', 1), ('G',1),
                     ('G', 1), ('F', 1), ('E', 1), ('D', 1),
                     ('C', 1), ('C',1), ('D', 1), ('E', 1),
                     ('E', 1.5), ('D', 0.5), ('D', 2),
                     ('E', 1), ('E', 1), ('F', 1), ('G',1),
                     ('G', 1), ('F', 1), ('E', 1), ('D', 1),
                     ('C', 1), ('C',1), ('D', 1), ('E', 1),
                     ('D', 1.5), ('C', 0.5), ('C', 2),
                     ('D', 1), ('D', 1), ('E', 1), ('C', 1),
                     ('D', 1), ('E', 0.5), ('F', 0.5), ('E', 1), ('C', 1),
                     ('D', 1), ('E', 0.5), ('F', 0.5), ('E', 1), ('D', 1),
                     ('C', 1), ('D', 1), ('G', 2),
                     ('E', 1), ('E', 1), ('F', 1), ('G',1),
                     ('G', 1), ('F', 1), ('E', 1), ('D', 1),
                     ('C', 1), ('C',1), ('D', 1), ('E', 1),
                     ('D', 1.5), ('C', 0.5), ('C', 2)]
            },
            'left_hand': {
                'options': {
                    'seconds_per_bar': 1.35, 
                    'frequency': 1200, 
                    'top_volume': 127.0,
                    'nblacks': 4.0
                },
                'tones': [('SILENCE', 2), ('C3', 4), ('G3', 4), ('C3', 4),
                        ('G3', 4), ('C3', 4), ('G3', 4), ('C3', 4),
                        ('G3', 2), ('C3', 2), ('G3', 4), ('G3', 4),
                        ('G3', 4), ('G3', 4), ('C3', 4), ('G3', 4),
                        ('C3', 4), ('G3', 2), ('C3', 2) ]
            }
        }

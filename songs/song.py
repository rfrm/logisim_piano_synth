# From https://www.wikiwand.com/es/Frecuencias_de_afinaci%C3%B3n_del_piano
TONE_FREQUENCY = {
        'SILENCE': 0,
        'C2': 65, 'E2': 82, 'A2': 110,
        'C3': 168, 'E3': 165, 'F3': 174, 'G3': 196, 'G#3': 207, 'A3': 220,
        'C': 261, 'D': 294, 'E': 330, 'F': 350, 'G': 392, 'G#4': 415, 'A4': 440, 'B4': 494,
        'C5': 523, 'E5': 659, 'D5': 587, 'D#5': 622, }

class Song(object):
    def sequences(self):
        raise NotImplementedError

    def song_name(self):
        raise NotImplementedError

    def create_sequences(self):
        sequences = self.sequences()
        for sequence in sequences:
            composed_sequence = self.compose(sequences[sequence]['tones'], **sequences[sequence]['options'])
            with open('%s_%s'%(self.song_name(), sequence), 'w') as f:
                f.write('v2.0 raw\n')
                f.write("\n".join(composed_sequence))

    def compose(self, tones, **kwargs):
        song = []
        seconds_per_time = kwargs['seconds_per_bar'] / kwargs['nblacks']
        samples_per_time = seconds_per_time * kwargs['frequency']
        for tone, tone_times in tones:
            samples = [tone] * int(samples_per_time * tone_times)
            nsamples = len(samples)
            volume = self.volume(kwargs['top_volume'], nsamples)
            song.extend((sample_volume << 16) | TONE_FREQUENCY[sample] for sample, sample_volume in zip(samples, volume) )
        return [format(sample, 'x') for sample in song]

    def volume(self, top_volume, nsamples):
        # return [int(i * delta) for i in range(nsamples, -1, -1)] 
        volume = [i**2 for i in range(nsamples, -1, -1)]
        m = max(volume)
        return [int(float(top_volume)*v/m) for v in volume]

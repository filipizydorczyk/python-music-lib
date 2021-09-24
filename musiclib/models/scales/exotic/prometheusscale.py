from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class PrometheusScale(Scale):
    """Prometheus can in music refer to both a scale 
    and a chord, the later is also known as the Mystic 
    chord (C Prometheus chord: C, F#, Bb, E, A, D). 

    :link: https://www.pianoscales.org/prometheus.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Oriental Scales for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(PrometheusScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
        ])

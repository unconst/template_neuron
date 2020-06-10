import tensorflow as tf


class Nucleus():
    def __init__(self, hparams, modelfn):
        self._hparams = hparams
        self._graph = tf.Graph()
        with self._graph.as_default(): 
            self._modelfn = modelfn
        self._session = tf.compat.v1.Session(graph = self._graph)

    def dispatch(self, batch):
        '''
        Args:
            batch: numpy_strings(batch_size, -1)
        Returns:
            dispatched: list[numpy_strings(-1, -1))
        '''
        return None

    def combine(self, dspikes):
        '''
        Args:
            dspikes: list(numpy_floats(-1, n_spikes))
        Returns:
            combined: numpy_floats(batch_size, n_combined)
        '''
        return None


    def spike(self, combined):
        ''' 
        Args:
            combined: numpy_floats(batch_size, n_combined)
                Combined downstream spikes from the gating network.
        Returns:
            spikes: numpy_floats(batch_size, n_spikes)
        '''
        #TODO (const): return the spike output from this node.
        return None

    def train(self, outputs, labels):
        pass

    def grade(self, up_grads):
        # no op: template node is not differentiable.
        pass




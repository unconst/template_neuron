
class Nucleus():
    def __init__(self, hparams):
        self._hparams = hparams
        self._graph = tf.Graph()
        with self._graph.as_default(): 
            self._modelfn = Modelfn(self._hparams)
        self._session = tf.Session(graph = self._graph)

    def dispatch(self, batch):
        '''
        Args:
            batch: numpy_strings(batch_size, -1)
        Returns:
            dispatched: list[numpy_strings(-1, -1))
        '''
        raise NotImplementedError

    def combine(self, dspikes):
        '''
        Args:
            dspikes: list(numpy_floats(-1, n_spikes))
        Returns:
            combined: numpy_floats(batch_size, n_combined)
        '''
        raise NotImplementedError


    def spike(self, combined):
        ''' 
        Args:
            combined: numpy_floats(batch_size, n_combined)
                Combined downstream spikes from the gating network.
        Returns:
            spikes: numpy_floats(batch_size, n_spikes)
        '''
        #TODO (const): return the spike output from this node.
        raise NotImplementedError

    def grade(self, up_grads):
        # no op: template node is not differentiable.
        pass




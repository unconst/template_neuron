class Neuron:
    def __init__(self, hparams, nucleus, dendrite):
        self._hparams = hparams
        self._nucleus = nucleus

    def static_spike(inputs):   
        raise NotImplementedError

    def _train(self):
        while True:
            self._train_step()

    def _train_step(self, batch, labels):

        to_network = self._nucleus.dispatch(batch)
        
        from_network = self._dendrite.query_network(dispatched)
        
        combined = self._nucleus.combine(from_network)

        outputs = self._nucleus.spike(combined)

        self._nucleus.train(outputs, labels)


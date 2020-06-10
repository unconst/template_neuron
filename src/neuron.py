class Neuron:
    def __init__(self, hparams, nucleus, dendrite, dataset):
        self._hparams = hparams
        self._nucleus = nucleus
        self._dataset = dataset
        self._dendrite = dendrite

    def static_spike(inputs):   
        raise NotImplementedError

    def start_training(self):
        batch, labels = self._dataset.next_batch()
        self._train_step(batch, labels)

    def _train_step(self, batch, labels):

        to_network = self._nucleus.dispatch(batch)
        
        from_network = self._dendrite.query_network(to_network)
        
        combined = self._nucleus.combine(from_network)

        outputs = self._nucleus.spike(combined)

        self._nucleus.train(outputs, labels)


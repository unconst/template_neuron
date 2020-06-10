

class Dendrite:
    def __init__(self, hparams):
        self._hparams = hparams
        self._channels = {}
        self._channel_ids = []
        self._channel_reliability = []
        self.connect()


    def connect(self):
        for node in self._metagraph.nodes.values():
            if node.identity == self._hparams.identity:
                continue
            elif node.identity not in self._channels:
                address = node.address + ':' + node.port
                self._channels.append(grpc.insecure_channel(address))
                self._channel_ids.append(node.identity)
                self._channel_reliability.append(0.5)

    def spike_network(self, outputs)
        logger.info('query')
        # 1. Create nounce.
        nounce = str(random.randint(0, 1000000000))

        # 2. Encode nounce and source
        source_id = self._hparams.identity
        nounce_bytes = bytes(nounce, 'utf-8')
        source_bytes = bytes(source_id, 'utf-8')
        spikes = numpy.array(['this is a test'])
        payload_bytes = pickle.dumps(spikes, protocol=0)

        # 3. Create unique message hash.
        hash = SHA256.new()
        hash.update(nounce_bytes)
        hash.update(source_bytes)
        hash.update(payload_bytes)
        message_id = hash.digest()

        # 4. Create futures.
        spike_futures = []
        for i,channel in enumerate(self._channels):
            try:
                stub = bittensor_grpc.BittensorStub(channel)
                request = bittensor_pb2.SpikeRequest(
                    version=1.0,
                    source_id=self._hparams.identity,
                    parent_id=self._hparams.identity,
                    message_id=message_id,
                    payload=payload_bytes)
                spike_futures.append(stub.Spike.future(request))
            except Exception as e:
                logger.error(str(e))

        # 5. Catch future responses
        start = time.time()
        exception = [False for _ in spike_futures]
        result = [False for _ in spike_futures]
        returned = [False for _ in spike_futures]
        timed = [0 for _ in spike_futures]
        while True:
            for i, future in enumerate(spike_futures):
                if future.done():
                    returned[i] = True
                    timed[i] = time.time() - start
                    try:
                        if future.exception():
                            exception[i] = True
                            failing_channels[i] = True

                    except Exception as e:
                        pass
                    try:
                        future.result()
                        result[i] = True
                    except Exception as e:
                        pass

            if time.time() - start > 3:
                break
            if sum(returned) == len(spike_futures):
                break

        for i in range(len(returned)):
            if returned[i]:
                r1 = self._channel_reliability[i]
                self._channel_reliability[i] = (r1 * 0.95) + (0.05 * 1)
            else:
                r1 = self._channel_reliability[i]
                self._channel_reliability[i] = (r1 * 0.95) + (0.05 * 0)
        
        return response


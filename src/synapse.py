import bittensor_proto.bittensor_pb2_grpc as bittensor_grpc
import bittensor_proto.bittensor_pb2 as bittensor_pb2
from loguru import logger

class Synapse(bittensor_grpc.BittensorServicer):
    def __init__(self, hparams, neuron, metagraph):
        self._hparams = hparams
        self._neuron = neuron

    def Spike(self, request, context):
        logger.info('{} --> S', request.source_id)
        inputs = numpy.asarray(pickle.loads(request.payload))
        outputs = self._neuron.spike(inputs)
        zeros_payload = pickle.dumps(numpy.zeros(outputs, protocol=0))
        response = bittensor_pb2.SpikeResponse(
            version=1.0,
            source_id=request.source_id,
            child_id=self._hparams.identity,
            message_id=request.message_id,
            payload=zeros_payload)
        return response

    def Grade(self, request, context):
        logger.info('{} --> G', request.source_id)
        return bittensor_pb2.GradeResponse(accept=True)




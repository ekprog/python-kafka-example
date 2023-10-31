import argparse
from kafka import EventBroker

if __name__ == '__main__':

    #
    # PARSING ARGUMENTS
    #
    parser = argparse.ArgumentParser(description='TestApp')

    parser.add_argument('type', type=str,
                        help='A required cunsumer/producer positional argument')

    parser.add_argument('--message', type=str,
                        help='An optional --message argument')

    parser.add_argument('--topic', type=str,
                        help='An optional --topic argument')

    parser.add_argument('--kafka', type=str,
                        help='An optional --kafka [ip:port] argument')

    args = parser.parse_args()

    #
    # ARGS VALIDATION
    #
    if args.type not in ['produce', 'consume']:
        raise Exception('Incorrect type argument (allows: produce/consume)')

    if len(args.kafka) == 0 or len(args.topic) == 0:
        raise Exception('Please specify --kafka and --topic arguments')

    if args.type == 'produce' and len(args.message) == 0:
        raise Exception('Empty --message for producing')

    # Any other rules...  :)
    # Please use execute command from ReadMe.md

    #
    # Simple DI
    #
    eventBus = EventBroker(args.kafka, args.topic)

    #
    # Bootstap (UCase layer)
    #
    if args.type == "produce":
        eventBus.produce(args.message)

    if args.type == "consume":
        eventBus.subscribe()


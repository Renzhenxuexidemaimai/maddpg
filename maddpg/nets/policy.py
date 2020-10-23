# -*- coding:utf-8 -*-

from maddpg.common.logger import logger
from maddpg.nets.mpl import mpl


def get_policy_model(id, args, act_shapes, obs_shapes):
    logger.info("create policy nets for agent: %d" % id)
    input_size = sum(obs_shapes)
    output_size = act_shapes[id]
    model = mpl(args.num_units, input_size, output_size, dropout=args.dropout)
    if args.print_net:
        model.summary()
    return model


if __name__ == '__main__':
    from maddpg.arguments import parse_experiment_args
    args = parse_experiment_args()
    m = get_policy_model(1, args, [2, 2, 2], [4, 4, 4])

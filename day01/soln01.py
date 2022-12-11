from functools import partial
import utils


if __name__ == '__main__':
    filename = 'input.txt'
    input_str_gen = utils.input_gen(filename)
    list_list_strs = utils.split_when(lambda s: s == '', input_str_gen)

    fcns = [lambda list_strs: map(int, list_strs), sum]
    chained_fcn = partial(utils.chain, fcns)
    in_order = sorted(map(chained_fcn, list_list_strs))
    print('solution 1:', in_order[-1])
    print('solution 2:', sum(in_order[-3:]))

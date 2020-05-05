from model import PopMusicTransformer
import os
import argparse
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

def main(num_samples, num_bars, temperature, prompt_dir ,output_dir):
    # declare model
    model = PopMusicTransformer(
        checkpoint='REMI-tempo-chord-checkpoint',
        is_training=False)

    from_scratch_path = output_dir + 'from_scratch/'
    with_prompt_path = output_dir + 'with_prompt/'
    
    if not os.path.exists(from_scratch_path):
        os.makedirs(from_scratch_path)
    if not os.path.exists(with_prompt_path):
        os.makedirs(with_prompt_path)

    for i in range(num_samples):
        # generate from scratch
        model.generate(
            n_target_bar=num_bars,
            temperature=temperature,
            output_path=from_scratch_path + '{}.midi'.format(i),
            prompt=None)

        # generate continuation
        model.generate(
            n_target_bar=num_bars,
            temperature=temperature,
            output_path= with_prompt_path + '{}.midi'.format(i),
            prompt=prompt_dir + f'{i:03}' + '.midi')

    # close model
    model.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate samples')
    parser.add_argument("--ns", default= 10, type= int, help= "number of samples")
    parser.add_argument("--nb", default= 16, type = int, help= "number of target bars")
    parser.add_argument("--t", default= 1.2, type = float, help= "temperature")
    parser.add_argument("--p", default= './data/evaluation/', type = str,help= " prompt directory")
    parser.add_argument("--o", default= './result/', type = str, help= "output directory")
    
    args = parser.parse_args()

    num_samples = args.ns
    num_bars = args.nb
    temperature = args.t
    prompt_dir = args.p
    output_dir = args.o


    print("Generating {} samples".format(num_samples))
    print("With {} target bars".format(num_bars))
    print("With {} temperature".format(temperature))
    print("Input promt root folder {}".format(prompt_dir))
    print("Output root folder {}".format(output_dir))
    main(num_samples,num_bars,temperature,prompt_dir, output_dir)

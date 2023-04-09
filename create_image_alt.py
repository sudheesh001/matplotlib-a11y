import matplotlib.pyplot as plt

for file_extension in ['png']:
    fig, ax = plt.subplots(nrows=1, ncols=1)
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ax.plot(X, Y, label='$X=Y$ Line')
    plt.savefig(f'dummy_image.{file_extension}',
                bbox_inches='tight',
                metadata={
                    'alt': f'This is an example description of the ALT text for the {file_extension} image'
                })

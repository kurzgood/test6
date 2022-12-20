import util

def main():
    f = open(snakemake.output[0],'w')
    f.write(util.get_time())
    f.close()

if __name__ == '__main__':
    main()
import argparse

def parse_fasta(fasta_path):
    with open(fasta_path) as f:
        header, seq = None, []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if header:
                    yield header, ''.join(seq)
                header = line
                seq = []
            else:
                seq.append(line)
        if header:
            yield header, ''.join(seq)

def write_fasta(records, output_path):
    with open(output_path, "w") as f:
        for header, seq in records:
            f.write(f"{header}\n")
            for i in range(0, len(seq), 60):
                f.write(seq[i:i+60] + "\n")

def trim_sequence(seq, f=None, l=None, t=None):
    if t is not None:
        if len(seq) <= t:
            return None
        return seq[:-t]
    else:
        start = (f - 1) if f else 0
        end = l if l else len(seq)
        if start >= len(seq) or start >= end:
            return None
        return seq[start:end]

def main():
    parser = argparse.ArgumentParser(description="Trim protein FASTA sequences")
    parser.add_argument("-f", type=int, help="First base to keep (1-based)")
    parser.add_argument("-l", type=int, help="Last base to keep (inclusive)")
    parser.add_argument("-t", type=int, help="Trim N residues from the end")
    parser.add_argument("-m", type=int, default=0, help="Minimum length of sequence to keep")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA file")

    args = parser.parse_args()

    if args.t is not None and (args.f or args.l):
        parser.error("Cannot use -t with -f or -l")

    trimmed_records = []
    for header, seq in parse_fasta(args.input):
        trimmed = trim_sequence(seq, f=args.f, l=args.l, t=args.t)
        if trimmed and len(trimmed) >= args.m:
            trimmed_records.append((header, trimmed))

    write_fasta(trimmed_records, args.output)

if __name__ == "__main__":
    main()

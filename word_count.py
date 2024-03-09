"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    file_names = glob.glob(f"{input_directory}/*.txt")
    df = pd.concat([pd.read_csv(file_name, sep="\t", header=None,
                   names=["word"]) for file_name in file_names], ignore_index=True)

    return df


def clean_text(dataframe: pd.DataFrame):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe["word"] = dataframe["word"].str.replace(
        r"[^\w\s\n\t]", "", regex=True)
    dataframe["word"] = dataframe["word"].str.lower()
    return dataframe


def count_words(dataframe: pd.DataFrame):
    """Word count"""
    df = dataframe.copy()
    df["word"] = df["word"].str.strip().str.split()
    df = df.explode("word", ignore_index=True)
    return df.value_counts().reset_index(name='count')


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep='\t', index=False)


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words(df)
    save_output(df, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )

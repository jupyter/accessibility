FROM mcr.microsoft.com/playwright:focal

RUN groupadd -r a11y && useradd --no-log-init -r -g a11y a11y
USER a11y

WORKDIR /home/a11y

RUN wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
RUN bash Mambaforge-$(uname)-$(uname -m).sh -b

COPY . .

EXPOSE 9323

CMD [ "bash" ]

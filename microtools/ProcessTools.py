import subprocess


class Process(object):
    def __init__(self, pipe):
        """

        :type pipe: subprocess.Popen
        """
        self.pipe = pipe

    def readLine(self):
        # type: () -> str
        line = self.pipe.stdout.readline()
        if line == '':
            return None
        return line


class ProcessResult(object):
    stdout = []
    stderr = []
    code = 1

    def __init__(self):
        self.stdout = []
        self.stderr = []
        self.code = 0

    def __str__(self):
        return "\n".join(self.stdout)


def execute(process, wait=True):
    """

    :type process: list[str] | str
    :type wait: bool
    :return:
    :rtype: ProcessResult|Process
    """

    pipe = subprocess.Popen(
        process, stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)
    if wait:
        res = ProcessResult()
        for line in pipe.stdout:
            res.stdout.append(
                line.strip()
            )
        return res
    else:
        return Process(pipe)

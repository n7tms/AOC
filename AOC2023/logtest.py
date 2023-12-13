import aoc_utils as aoc

part = 1


aoc.logger.level=aoc.logging.WARNING
# aoc.logger.level=aoc.logging.INFO

aoc.logger.debug('testing this.')
aoc.logger.info(f'Part {part}')
aoc.logger.critical(f'something bad??')

aoc.logger.info(f'not so bad')


lgr = aoc.logger.getChild('2023')
lgr.warning(f'hello warning')
lgr.setLevel = 50
lgr.info(f'hello info')

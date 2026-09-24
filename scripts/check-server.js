try {
  const response = await fetch(process.argv[2], { signal: AbortSignal.timeout(500) });
  const html = await response.text();
  process.exitCode =
    response.ok &&
    html.includes('name="urchin-skipper-app" content="deck-playtest"') &&
    (!process.argv.includes('--production') ||
      response.headers.get('x-urchin-build') === 'production')
      ? 0
      : 1;
} catch {
  process.exitCode = 1;
}

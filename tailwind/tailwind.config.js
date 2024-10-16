module.exports = {
  content: [
    '../app/templates/**/*.html',
    '../app/static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        custom: {
          gradient: 'linear-gradient(to top left, #AC32E4, #7918F2, #4801FF)',
          background: 'hsl(299, 50.05%, 4.4%)',
          foreground: 'hsl(299, 7.7%, 97.75%)',
          muted: 'hsl(299, 38.5%, 16.5%)',
          'muted-foreground': 'hsl(299, 7.7%, 55.5%)',
          popover: 'hsl(299, 49.6%, 7.15%)',
          'popover-foreground': 'hsl(299, 7.7%, 97.75%)',
          card: 'hsl(299, 49.6%, 7.15%)',
          'card-foreground': 'hsl(299, 7.7%, 97.75%)',
          border: 'hsl(299, 38.5%, 16.5%)',
          input: 'hsl(299, 38.5%, 16.5%)',
          primary: 'hsl(299, 77%, 55%)',
          'primary-foreground': 'hsl(299, 7.7%, 5.5%)',
          secondary: 'hsl(299, 38.5%, 16.5%)',
          'secondary-foreground': 'hsl(299, 7.7%, 97.75%)',
          accent: 'hsl(299, 38.5%, 16.5%)',
          'accent-foreground': 'hsl(299, 7.7%, 97.75%)',
          destructive: 'hsl(0, 62.8%, 30.6%)',
          'destructive-foreground': 'hsl(299, 7.7%, 97.75%)',
          ring: 'hsl(299, 77%, 55%)',
        },
      },
    },
  },
  plugins: [],
}